下面我们就在本机搭建一个Hadoop环境。

1 安装配置Hadoop
首先下载Hadoop的压缩包，http://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-2.8.3/hadoop-2.8.3.tar.gz
下载地址:北京信息学院镜像http://mirror.bit.edu.cn/apache/hadoop/common/
我这里使用的是2.8.3版本，下载好后解压到某文件夹。

Hadoop依赖于java，所以需要首先在电脑上装好java，配好java的环境变量。

配置Hadoop环境变量
hadoop的可执行文件在sbin目录和bin目录，我们需要将这两个目录配到环境变量Path里。

以mac为例，看环境变量配置，vi .bash_profile ：

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_251.jdk/Contents/Home
export HADOOP_HOME=/Users/getech/Downloads/hadoop-2.8.5
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_HOME}/lib/native
export HADOOP_OPTS="-Djava.library.path=${HADOOP_HOME}/lib/native/"
配置完毕后，source .bash_profile使环境变量生效。执行hadoop version

weifengdeMacBook-Pro:~ wuwf$ hadoop version
Hadoop 2.8.5
Subversion https://git-wip-us.apache.org/repos/asf/hadoop.git -r 0b8464d75227fcee2c6e7f2410377b3d53d3d5f8
Compiled by jdu on 2018-09-10T03:32Z
Compiled with protoc 2.5.0
From source with checksum 9942ca5c745417c14e318835f420733
This command was run using /Users/aiot/Downloads/hadoop-2.8.5/share/hadoop/common/hadoop-common-2.8.5.jar

Hadoop的各个配置文件
各文件均在hadoop安装目录下etc/hadoop下

修改hadoop-env.sh
加入  export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home

后面是你的Java_HOME的路径。

修改core-site.xml
<configuration>
<!--设置临时目录-->
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/Users/aiot/Downloads/hadoop-2.8.5/</value>
    </property>
    <!--设置文件系统-->
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>

上面临时目录是本地的一个目录，下面的ip是本机的ip，注意用localhost时后面报错，需要直接填写自己的ip。

修改hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
只有本机一个节点，设置replication为1

添加mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
在目录下创建一个该文件，填入上面的内容

配置yarn-site.xml
<configuration>

<!-- Site specific YARN configuration properties -->
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.resourcemanager.address</name>
        <value>10.8.32.13:9999</value>
    </property>
</configuration>

启动Hadoop
先执行：hadoop namenode -format

然后启动hdfs：start-dfs.sh，如果mac电脑显示localhost port 22：Connect refused，需要在设置-共享-勾选远程登录，允许访问那个添加当前用户。

执行start-dfs.sh后会要求输入3次密码。

然后：start-yarn.sh

两个命令执行后，通过浏览器访问：localhost:50070


代表hadoop配置成功。

推送文件到hadoop中
执行如下命令

hdfs dfs -mkdir /wc

hdfs dfs -put a /wc/1.log

hdfs dfs -put a /wc/2.log

hdfs dfs -put a /wc/3.log

先在hdfs上创建一个目录，然后推送本机的文件a到hdfs上，并重新命名。

hdfs dfs -ls /wc  可以查看目录下的文件。

spark读取hadoop文件
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;

import java.util.List;

/**
 * @author wuweifeng wrote on 2018/4/27.
 */
public class Test {
    public static void main(String[] args) {
        SparkSession sparkSession = SparkSession.builder().appName("JavaWordCount").master("local").getOrCreate();

        JavaSparkContext javaSparkContext = new JavaSparkContext(sparkSession.sparkContext());
        JavaRDD<String> javaRDD = javaSparkContext.textFile("hdfs://192.168.1.55:9999/wc/1.log");
        //取10%的数据，随机数种子自己设定，也可以不设定
        JavaRDD<String> sample = javaRDD.sample(false, 0.1, 1234);
        long sampleDataSize = sample.count();
        long rawDataSize = javaRDD.count();
        System.out.println(rawDataSize + " and after the sampling: " + sampleDataSize);

        //取指定数量的随机数据
        List<String> list = javaRDD.takeSample(false, 10);
        System.out.println(list);

        //取排序好的指定数量的数据
        List<String> orderList = javaRDD.takeOrdered(10);
        System.out.println(orderList);
    }
}
同样是使用textFile方法，和操作本地文件一样。


https://blog.csdn.net/tianyaleixiaowu/article/details/80116855
bash: ls: command not found的解决办法
命令无法使用时候 
export PATH=/bin:/usr/bin:$PATH



/usr/local/Cellar/hadoop/3.2.1_1/libexec

WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable


解决办法 https://www.cnblogs.com/likui360/p/6558749.html
https://blog.csdn.net/ligt0610/article/details/47757013
解决https://blog.csdn.net/ligt0610/article/details/47757013
macOS 下体验 Hadoop
 https://www.jianshu.com/p/2f80806a3b6d
 
 

4 端到端的构建信息安全管理体系和技术体系，筹备自研，并规划下一代物联网业务安全产品体系
5 站在公司业务战略、突破变革、业务视角的基础上导入TOGAF


Mac 安装 hadoop+hive+hbase+spark