# Systems Realization of Multimodal Agent Memory：设计记录

图产物：`latex/figures/systems_realization.{pdf,svg,png}`
生成脚本：`code/gen_systems_realization.py`
绘制日期：2026-09-04 PT

## 1. 图与章节的对应

图对应 survey §7.5 Memory Infrastructure and Efficiency，术语直接取自正文，
不另造词：

| 图上区块 | 正文出处 | 承担的论点 |
| --- | --- | --- |
| 左：Logical Memory 四类卡片 | §7.5.1 / §3 | 逻辑类型由 operative representation 定义 |
| 中：Cross-Layer Memory Runtime | §7.5.4 | read 路径 materialize，write 路径 commit |
| 右：Active Model Execution | §7.5.1 | materialized execution state 不自动等于 memory |
| 底：Physical Memory Hierarchy | §7.5.2 | residency 与 data movement，与逻辑类型正交 |
| 顶：Indexing, Reuse & Scheduling | §7.5.3 | 逻辑索引与执行态索引是两个查找问题 |
| 右侧竖条：Consistency & Coordination | §7.5.4 | identity/version/provenance/dependency 跨层成立 |

## 2. 设计决策

每条记：问题、选定做法、理由、如何回滚。

### D1 write path 画成右到左的镜像

- 问题：需求文档按 `Execution History -> Summarize/Compress/Encode ->
  Commit and Write-back` 顺序列出，若照抄从左往右画，写回箭头会指向执行侧，
  与语义反向。
- 做法：write 路径镜像成右到左，与 read 路径构成闭环；两行 pill 宽度
  关于中心严格对称（read 150/215/175，write 175/215/150，about x=806）。
- 理由：闭环是 §7.5.4 的实际结构（memory 出去、执行史回来）；镜像同时满足
  "两条路径视觉对称" 的要求。
- 回滚：把 `gen_systems_realization.py` 中 write 行三个 `pill()` 的 x 与
  两个 `line()` 的方向对调即可，约 6 行。

### D2 左侧连接改成 elbow，接在卡片间隙

- 问题：初版用直箭头连接 Logical Memory 与 runtime，read 箭头恰好指向
  Source & Modality-Specific 卡、write 箭头恰好指向 Latent & Parametric 卡，
  读者会误解为 "读只读源模态、写只写潜在记忆"。
- 做法：两条连接改成折线，落点移到卡片之间的空隙（y=308 与 y=386），
  表达 "整个 panel"。同时把左 panel 宽度从 446 收到 422，腾出 46 单位的
  连接通道，控制面总线走 x=462，折线竖段走 x=478。
- 理由：图必须在无 caption 时也不产生错误读法。
- 回滚：把两条 `<path>` 换回 `line(472, y, 506, y)` 形式。

### D3 字号按 survey 自身插图标定

- 问题：初版画完自查，图放到正文宽时最小字号约 2.6 pt，不可读。
- 做法：用 PyMuPDF 抽取 survey Figure 1 与 Figure 5 的 span 字号，得到基准
  "图宽 506 pt，图内字号 4.3 pt（最小）到 7.5 pt（panel 标题）"。据此重排：
  删掉自加的次要副标、加宽 action pill、右栏输入由 2x2 改单列、缩短过长文案，
  空间全部让给字号。终版阶梯（figure units / 折算 506 pt 图宽）：
  13.5-14 / 4.1-4.2 pt（例子与副标），15-17 / 4.5-5.1 pt（主标签），
  24-26 / 7.2-7.8 pt（区块标题）。
- 理由：图的可读性要与同一篇论文的其它图一致，凭感觉调字号会系统性偏小。
- 复现基准：
  ```bash
  python3 -c "
  import pymupdf, collections
  p = pymupdf.open('<survey>.pdf')[8]
  c = collections.Counter()
  for b in p.get_text('dict')['blocks']:
      for l in b.get('lines', []):
          for s in l['spans']:
              if 150 < s['bbox'][1] < 560: c[round(s['size'],1)] += len(s['text'].strip())
  print(sorted(c.items()))"
  ```
- 回滚：字号是脚本里的字面量，整体缩放改一遍即可；但改小之前先重跑上面的
  基准命令，不要凭感觉。

### D4 PDF 由 Chrome headless 导出，不用 rsvg-convert

- 问题：`rsvg-convert -f pdf` 的产物含 13 个 Type3 字体。arXiv 对 Type3 告警，
  IEEE PDF eXpress 直接拒。
- 做法：把 SVG 包进一个设了 `@page size: 17.5in 8.3333in` 的 HTML，用
  `chrome --headless --print-to-pdf` 导出，产物 17 个字体全为 Type0 子集，
  页面 1260x600 pt，比例 2.1:1。已固化在 `code/build.sh`。
- 校验：
  ```bash
  python3 -c "
  import pymupdf
  p = pymupdf.open('latex/figures/systems_realization.pdf')[0]
  print(sum(1 for f in p.get_fonts() if f[2]=='Type3'))"
  ```
  期望输出 0。
- 回滚：若换机器没有 Chrome，可用 Inkscape `--export-text-to-path` 把文字转
  曲线后再导 PDF；不要退回 rsvg 的 PDF 路径。

### D5 仓库布局与命名

- 做法：仓库名 `mm-agent-memory-survey-figures`，按全局默认布局分
  `code/`（生成脚本与构建）、`latex/figures/`（产物）、`docs/`（本文件）。
  产物入 Git 而非 HF：总计约 1 MB 的图片与文本，且是论文资产不是可复用数据集。
- 回滚：改名或迁并入 survey 主仓库都只是 `git mv` 加改 remote，成本几分钟。

## 3. 约束核对

需求里的五条禁止项，逐条落实位置：

| 约束 | 落实方式 |
| --- | --- |
| 不出现论文名 | 图内无任何 paper name |
| 不像神经网络架构图 | 无层堆叠、无张量流，全部为容器与路径 |
| 不暗示长期记忆总在慢存储 | 底部横带标题旁写明 placement 与 representation 正交；无任何一层被标为 long-term memory |
| 不暗示所有 KV cache 都是 agent memory | 右栏 callout：request-local state 是执行产物，只有被刻意保留复用的才成为 memory |
| 不把 vector database 当作独立逻辑类型 | 全图不提 vector DB；页脚写明 indices and stores realize access without defining a new memory type |

## 4. 已知取舍

- 图信息密度高于 survey 现有插图，最小字号（4.1 pt）压在基准区间下沿。
  若印刷版仍嫌小，优先删次要副标（`READ_EX`/`WRITE_EX` 的第二行、
  tier 的 sub 行），而不是继续缩排版。
- `Summarize · Compress ·` 在 pill 内折行，第一行以间隔号结尾。
  若不接受，把该 pill 加宽到 260 并把 read 行的 `Materialize` 同步加宽保持镜像。
