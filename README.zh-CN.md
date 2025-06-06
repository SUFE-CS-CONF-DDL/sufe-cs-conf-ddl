# sufe-cs-conf-ddl

一款帮助上财信息人能更好地追踪院标常任轨🎰计算机会议截稿日期⏳的工具🔧。我们提供了一个双重检索系统来过滤出您真正关心的那个会议⏰。

如果您觉得对您的研究有所帮助，欢迎收藏❤️[网址](https://sufe-cs-conf-ddl.github.io/)，分享并星标🌟本项目!

请参考[本网址](https://github.com/lixin4ever/Conference-Acceptance-Rate) 查询不同会议接受率 。

希望大家都能论文高中🎉科研成果爆表⌚️！
## 示例:

[![示例预览](.conf_list/screenshot.png)](https://github.com/SUFE-CS-CONF-DDL/sufe-cs-conf-ddl/blob/main/.conf_list/screenshot.png)

## 会议格式文件
会议的yaml示例文件格式：

```yaml
- title: SIGIR
  description: International Conference on Research on Development in Information Retrieval
  sub: DBIR
  rank: A
  TierLevel: Second
  dblp: sigir
  confs:
    - year: 2021
      id: sigir21
      link: http://sigir.org/sigir2021/
      timeline:
        - abstract_deadline: '2021-02-02 23:59:59'
          deadline: '2021-02-09 23:59:59'
      timezone: AoE
      date: July 11-15, 2021
      place: Virtual
    - year: 2022
      id: sigir22
      link: https://sigir.org/sigir2022/
      timeline:
        - abstract_deadline: '2022-01-21 23:59:59'
          deadline: '2022-01-28 23:59:59'
      timezone: AoE
      date: July 11-15, 2022
      place: Madrid
```
注意：YAML文件应当严格按照格式缩进要求，推荐用Sublime/Pycharm等进行文本编辑，会进行报错。

以上脚本项目的描述：

> **yaml项目的描述**
>
> - `title`: 会议大写缩写名称, i.e. SIGIR
> - `descripition`: 会议全名, i.e. International Conference on Research on Development in Information Retrieval
> - `sub`: 会议在常任轨会议列表中的类别，与CCF分类基本类似. i.e. DBIR. 可参考下表
> - `rank`: 会议的[CCF级别](https://www.ccf.org.cn/c/2019-04-25/663625.shtml). i.e. A
> - `TierLevel`: 上财信管常任轨会议名单的[Tier级别](https://github.com/SUFE-CS-CONF-DDL/sufe-cs-conf-ddl/blob/main/.conf_list/SIME_tenure_CCF.xlsx) i.e. Second Tier.
> - `dblp`: 会议的dblp网址后缀, 通常为会议的小写缩写. i.e. https://dblp.uni-trier.de/db/conf/sigir
> - `confs`:
    >   - `year`: 举办年份, i.e. 2022
>   - `id`: 会议名称&举办年份后两位, i.e. sigir22
>   - `link`: 会议主页网址. i.e. https://sigir.org/sigir2022/
>   - `timeline`:
      >     - `abstract_deadline*`: 会议摘要截止时间，非必要. i.e. '2022-01-21 23:59:59'
>     - `deadline`: 形如`yyyy-mm-dd hh:mm:ss` 或 `TBD`的确切截止时间, i.e. '2022-01-28 23:59:59'
>     - `comment*`: 额外辅助信息，非必要. i.e. comment: The final round of paper submission.
>   - `timezone`: 会议截止时间的时区. 只识别 UTC±X 或 AoE(UTC-12)格式, 其他所有时区应转化为 UTC 格式, 比如 EST=UTC-5.
>   - `date`: 会议的具体举办日期, i.e. July 11-15, 2022
>   - `place`: 会议的具体举办地点, i.e. Madrid, Spain/Virtual
>
> 未标注（*）的项目是yaml脚本的必要项目。

会议分类表:
> - 并行与分布计算
    >   sub: PDC
> - 计算机图形学与多媒体
    >   sub: CGM
> - 理论计算机
    >   sub: TC
> - 人工智能
    >   sub: AI
> - 软件工程
    >   sub: SE
> - 数据库与信息检索
    >   sub: DBIR
> - 网络与信息安全
    >   sub: NIS

## 添加新的会议方向和更新截止日
我们非常欢迎并十分感激您能在本项目组中提出贡献。🤟

添加新的会议方向和更新截止日的步骤
- Fork这个项目仓库.
- 通过提交会议的`yaml`文件来添加新的会议方向和更新截止日
- 提交[Pull Request](https://github.com/SUFE-CS-CONF-DDL/sufe-cs-conf-ddl/pulls).

👨‍🏫 如果您对P&R操作不熟悉的话可以参考[本网址](https://chinese.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github/) 。


P&R后步骤：
1. 在本local工程项目下面git pull
2. Run `python merge_all.py`
3. Run `npm run build`
4. dist文件夹中的内容拖到`sufe-cs-conf-ddl.github.io`下面，push上去。


## 贡献

本项目当前由 [@SUFEHeisenberg](https://github.com/SUFEHeisenberg) 在 [@HuipingXie](https://github.com/HuipingXie) 帮助下创建👨🏻‍💻。 

如果您喜欢本项目，能够为[@HuipingXie](https://github.com/HuipingXie) 介绍个女朋友👧的话我们将不胜感激!

如果您对共同维护本项目感兴趣，欢迎[邮箱私信](mailto:wangziyuan@163.sufe.edu.cn)👏。

灵感启发来自以下优秀项目：
- [ai-deadlines](https://aideadlin.es/) 
- [ccfddl](https://ccfddl.github.io/)