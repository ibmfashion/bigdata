# bigdata
1 Docker 安装Hadoop HDFS命令行操作 https://www.cnblogs.com/hongdada/p/9488349.html
  搭建Hadoop单机环境，使用spark操作Hadoop文件  https://cloud.tencent.com/developer/article/1384094
2 云原生“Cloud Native”就是一开始开发的时候就是为了最终部署到云环境上的。
  代表技术包括容器（Container）、服务网格（Service Mesh）、微服务（Microservice）、不可变基础设施（immutable infrastructure）和声明式API（declarative APIs）。其中容器（Container）是k8s的底层引擎，服务网格（Service Mesh）是建立在k8s上的针对请求的扩展功能，不可变基础设施（immutable infrastructure）是现代运维的基石，声明式API（declarative APIs）是k8s的编码方式
  云技术的三大基石：
  基础设施即代码 (Infrastructure As Code）
  基础设施即代码是指把创建基础设施（包括服务器和网络环境）的命令像应用程序一样储存在源码库中，并进行版本管理。这样创建基础设施的过程就变成了部署软件的过程。它的最大的好处就是可重复性。以前的方法是用人工敲入命令来创建运行环境，出了问题就在原来的基础之上进行修修补补，一旦需要把整个环境重新建立，很难保证与原来的一样。 当使用基础设施即代码之后，再也没有了这个担心。
  
  详情请见 InfrastructureAsCode
  
  不可变基础设施（immutable infrastructure）
  说道这里，我们不得不提“不可变基础设施（immutable infrastructure）“，它是基础设施即代码的升级版。有了基础设施即代码之后，随时都可以通过运行软件再构建出一个一模一样的服务器和其他需要的设备，并且还能预装应用程序，创建的时间还是秒级的。这时当服务器出现问题时，就没有必要去花时间查找原因了并修复了，而是直接把服务器销毁重新创建一个新的。因此这时的基础设施是不可变的，只有创建和删除，而没有修改操作。这彻底改变了运维的方式。
  
  详情请见 What is "Immutable Infrastructure"?
  
  声明式API（declarative APIs）
  声明式API也是基础设施即代码的升级版。最开始时，当用软件定义基础设施时是用的过程式描述，也就是通过运行一系列的命令来创建运行环境。后来发现更好的办法是描述最终运行环境的状态，而由系统来决定如何来创建这个环境。例如，你的描述就变成“创建一个有三个Nginx的集群”，而不是把创建Nginx的命令运行三次组成一个集群。这样的好处是当运行环境与描述不符合时，系统能检测到差异，并自动修复，这样系统就有了自动容错的功能。
3 Kubernetes 应用场景比较适合进行容器化改造，比如无状态的应用、对可伸缩性要求比较高的应用和对快速迭代开发要求较高的应用。而其他的应用场景，如中台和前台的应用比较无状态并有伸缩性要求，后端应用实际上状态比较多，这些有状态应用在容器化方面的进展则比较缓慢。
  将所有机器都变成一个大集群来管理，这一理念来源于谷歌大规模集群管理器Borg，这样的设计思想让用户无需关注资源管理的问题，并且实现了跨多个数据中心的资源利用率最大化。
  智慧城市中就包含着大量边缘计算的应用场景。这些边缘节点产生的数据同样需要收集处理，但由于部分边缘节点的位置比较偏僻而导致带宽不是很高，必须在本地处理数据，这也是Kubernetes值得关注和探索的一个重要方向。
4 边缘计算 随着5G、IoT的标准化工作越来越完善，边缘计算得到了长足的发展 k3s和业界首个Kubernetes操作系统k3OS

5 数字化转型
  80%的企业在推动数字化转型时会遇到下列5道坎：
  
  1.小规模测试无法扩及全组织。许多组织通常只在销售、研发等特定部门中，导入规模非常小的测试，但这些测试计划通常不是以企业的全体营运为考量，最后反而会成为“拼装车”，无法套用至组织的整体转型。
  
  2.难以找到对的策略伙伴。由于物联网涉及到许多技术，不可能只找一个合作伙伴，就完成所有系统和流程的建置，但对于企业来说困难的是市场上有太多选择，难以判断谁才能提供得以运行的服务。
  
  3.错误的领导与组织设计。提到导入物联网，多数管理者第一个念头是由IT部门主持，但麦肯锡总结成功经验指出，由业务部门带领会是更好的做法，避免其他营运单位认为这只跟技术有关，而无法产生动力共同参与。
  
  4.沟通过程繁多与琐碎。转型过程会涉及许多跨部门沟通，但这些步骤往往繁琐，牵涉的对象也很多，导致不够顺畅的沟通，自然也难以建立共识。
  
  5.员工职能及工作方式无法跟上。企业常会有一个误解，认为只要导入完整的平台或设备就已足够，却忽略了内部员工的能力及工作方式，所以常常导致转型失败。
  
  利用数字化技术和能力来驱动组织的商业模式创新和商业生态系统重构的途径和方法，其目的是实现企业业务的转型、创新、增长。
  
  让IT系统数字化平台为业务变革铺好道路，使业务快速响应市场变化；
  全方位描述流程，并转换为IT系统数字化平台的关键需求，确保战略落地；
  有效管理并监控企业的流程，快速定位企业流程的变化，及对企业业务、组织、人员、IT系统影响。
  
  缺乏企业架构的公司各IT系统犹如一个个孤立的"竖井"，需要大量的加工、清洗，才能保持一致性。
  …or create a new repository on the command line
  echo "# bigdata" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git remote add origin https://github.com/ibmfashion/bigdata.git
  git push -u origin master
                  
  …or push an existing repository from the command line
  git remote add origin https://github.com/ibmfashion/bigdata.git
  git push -u origin master
  …or import code from another repository
  You can initialize this repository with code from a Subversion, Mercurial, or TFS project.