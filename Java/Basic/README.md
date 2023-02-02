## Java 流

### 大致的分类：

IO流：

1. 字节流
   - InputStream
   - OutputStream
2. 字符流
   - Reader
   - Writer

字节流一次读取一个字节 1Byte，最终父类为上述的两个Stream

字符流一次读取一个字符 2Byte，最终父类为上述的两个er

### 文件流

下面这两个流是字节流，使用 `read()` 方法一次读一个字节, `write()` 同理；并且，这两个流是低级流，可以直接使用，无需串联其他流

**FileInputStream：**

- `new FileInputStream(new File(path))`
- `new FileInputStream(path)`

- `int read()`：一次只读取一个字节。

- `int read(byte[] b)`：一次读取一个字节数组的字节。

- `int read(byte[] b, int offset, int len)`：一次读取len个字节，然后放入字节数组的offset下标开始处。

**FIleOutputStream:**

- `new FileOutputStream(new File(path), isAppend)` 第二个参数表示是否为append模式
- `new FileOutputStream(path, isAppend)`

- `void write()`：一次写出一个字节。

- `void write(byte[] b)`：一次写出一个字节数组。

- `void write(byte[] b, int offset, int len)`：把字节数组中从下标offset开始的字节写出文件，并且写出len个长度。

写入时，可以使用 `getBytes()` 方法将字符串转成byte数组，并且可以指定编码集，例如utf-8

### 字节缓冲流

字节缓冲流是一个高级流，需要搭配低级流使用

BufferedInputStream(InputStream in): 这里的in代表一个低级流

BufferedInputStream(InputStream in, int size): size表示缓冲区大小，默认8K

BufferedOutputStream(OutputStream in)

BufferedOutputStream(InputStream in, int size)

其余使用方法与文件流一致，使用`read()` 与 `write()` 读取字节数组即可

**局别**：缓冲流存在一个 `flush()` 方法，将缓存区的数据刷进磁盘，这样做的目的是为了减少IO消耗，因此如果不主动调用该方法，或未关闭缓冲流，文件不会被写数据，但使用文件流时，文件会被写数据；对于缓冲区，缓冲区满则进行一次 `flush()` 操作，清空缓冲区写文件；

此外，对于串联的流，关闭最外层流即可，内层流会被自动关闭

### 对象流

参数是一个输入输出流，但不限定是高级流或者低级流，但是最终必须连接至一个低级流上（嵌套），这个流关系到Java对象的序列化与反序列化

**ObjectInputStream(InputStream in)**

**ObjectOutputStream(InputStream out)**

- `Object readObject()`：该方法是将从文件中读取到的字节数组转换为对象。
- `Void writeObject(Object obj)`：该方法将对象数据转换为一组字节数组，然后写出到文件中。

### 字符转换流

字符转换流用于进行字节与字符流之间的转换中间流，以字符作为读写单位，只能适合读写文本数据，但是，底层仍用字节流进行数据读取，中间进行转化和包装成为字符；该流是高级流，通常用于连接不同的流；字符流父类是 `Reader` 以及 `Writer`

- `InputStreamReader(InputStream in)`

- `InputStreamReader(InputStream in, String csn) `：此处csn可以传入一个字符集
- `OutputStreamWriter(OutputStream out)`
- `OutputStreamWriter(OutputStream out, String csn) `

- `read()` ：方法可以读取一个字符，即2个字节 2 Bytes
- `write(str)` ：这个方法可以直接传入字符串写入

### 字符缓冲流

带缓冲区的字符输入缓冲流

- `BufferedReader(Reader in)` ：这里的in是一个字符输入流

- `BufferedReader(Reader in, int size)`：这里的size是缓冲区大小，默认8K

用于读取文件的文本内容？（存疑），一般搭配文件流和字符转换流使用，三层嵌套，但是好处是可以使用：

- `readline()` ：读取一行的内容，以字符串形式返回；返回 `null` 时代表文件结束

字符输出缓冲流：

- `BufferedWriter(Writer out)`
- `BufferedWriter(Writer out, int size)`：和所有的缓冲流一样，缓冲区大小默认8K

不过，这里的输出流经常与下面的 `PrintWriter` 一起使用（**注意，这里是使用最外层的PrintWriter，内部传入BufferedWriter使用**），该流带有自动行刷新的功能，也可以继续与低级流串联使用，当然也可以单独使用，非常强大；其中若传入了流，则可以设置自动刷新的布尔值；自动刷新的含义指：使用 `println(string)` 时，自动 `flush()` ，直接写入，当然也可以直接使用 `print(string)` 进行不换行的写入string；这里都是文本字符写入，因此不需要转化为字节数组。

```java
PrintWriter(Writer out)

PrintWriter(Writer out, boolean autoflush)

PrintWriter(OutputStream out)

PrintWriter(OutputStream out, boolean autoflush)

PrintWriter(String filename, String csn)

PrintWriter(File file)

PrintWriter(File file, String csn) 
```



## Java 反射机制

目前看到的其中一个作用是，需要根据类信息生成实例时，例如AOP或动态代理，不用编写固定的代码，而是通过反射加载某一个类，再创建实例；

反射拥有以下四大功能：

- 在运行时（动态编译）获知任意一个对象所属的类。
- 在运行时构造任意一个类的对象。
- 在运行时获知任意一个类所具有的成员变量和方法。
- 在运行时调用任意一个对象的方法和属性。

### 得到类对象 Class 的方法

1. `Class alunbarClass = TargetObject.class;`：该方法需要知道需要的类，然后调用.class获取Class对象，不常用；因为上述情况下，我们不知道需要的类；

2. `Class alunbarClass1 = Class.forName("com.xxx.TargetObject");` ：通过一个类的全限定名获取，比较常见；这种情况下，默认会进行类的初始化（详见JVM的ClassLoader），意义是这个类的Static部分代码会被执行；

3. ```java
   Date date = new Date();
   Class alunbarClass2 = date.getClass();
   // 这是通过一个实例直接获取其Class对象
   ```

4. `class clazz = ClassLoader.LoadClass("com.xxx.TargetObject");`：通过类加载器加载

### 类对象创建实例的方法

1. `Class.newInstance();` 使用Class对象的该方法创建一个实例；可以注意到这里没有参数，实际上需要调用该实例对象的**无参构造器**，如果没有无参构造则会抛出一个异常；另外，如果无参构造器是private的，也不能进行访问；

2. `Constructor.newInstance(args);` 很明显，这个方法需要先获得该类的构造器，然后使用构造器进行实例化；这时可以避免没有无参构造器的问题；想要获得构造器，可以使用Class对象的这些方法：

   ```java
   // 返回所有public构造方法，即可访问到的构造器
   public Constructor[] getConstructors() { }
   // 返回所有构造方法
   public Constructor[] getDeclaredConstructors() { }
   //  返回一个指定参数的public构造方法
   public Constructor getConstructor(Class... parameterTypes) { }
   //  返回任意一个指定参数的构造方法
   public Constructor getDeclaredConstructor(Class... parameterTypes) { }
   
   // 想返回无参构造器，可以传入null
   Constructor constructor = clazz.getConstructor(null);
   MyObject obj = (MyObject) constructor.newInstance();
   
   // 想使用私有构造器或方法，取消安全检查
   Constructor constructor = clazz.getDeclaredConstructor(int.class);
   constructor.setAccessable(true);
   MyObject obj = (MyObject) constructor.newInstance(114514);
   
   ```

### 类对象获取成员变量的方法

```java
// 类似于获得构造器，分为获得公有字段以及全部字段
public Field[] getFields() { }
public Field[] getDeclaredFields() { }

// 想要获得单个字段，需要传入字段名
public Field getField(String name) { }
public Field getDeclaredField(String name) { }

// 使用反射方法修改变量，需要得到该对象实例，以及修改字段对象，使用set方法进行修改；当然，修改私有变量时，需要取消安全检查
Field field = clazz.getField("name");
Object obj = constructor.newInstance();
field.set(obj, "newName");
```

### 类对象获取成员方法并调用

```java
// 同理，不再赘述
public Method[] getMethods() { }
public Method[] getDeclaredMethods() { }
// 注意，这里第一个参数为方法名，下面是它的参数对应的类
public Method getMethod(String name, Class<?>... parameterTypes)
public Method getDeclaredMethod(String name, Class<?>... parameterTypes)
    
// 举例：获取一个show(str)的方法
Method method = clazz.getMethod("show", String.class);

// 想要调用方法，使用invoke进行调用，后面传入参数即可，类似于set方法
method.invoke(obj, "Soudayo");

```

### 反射的优缺点

- 优点：灵活，在**运行时**动态获取类的实例
- 缺点：效率低下，毕竟没有经过优化，直接解释，性能不如编译+解释+优化；此外还存在安全性问题，破坏了封装性，例如调用私有方法，访问私有成员变量等；

### 常用的应用场景

- 动态代理机制

- 使用 JDBC 连接数据库：

  - `Class.forName("com.mysql.jdbc.Driver"); `：一般来说，这种引用了包名+类名的场景里都使用了反射去加载类

- Spring / Hibernate 框架（实际上是因为使用了动态代理，所以才和反射机制有关）

  - 最典型的就是 Spring 通过 xml 配置文件装载 Bean（创建对象），也就是 **Spring 的 IoC**，过程如下：

    - 加载配置文件，获取 Spring 容器 `ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");`

    - 使用**反射机制**，根据传入的字符串获得某个类的 Class 实例 `Service service = (Service) ac.getBean("service Impl");`

  - AOP中因为涉及到动态代理，也需要引入反射机制



## Java 动态代理

静态代理的实现方式：

1. 定义接口，用于定义代理以及被代理类的行为；

2. 编写被代理类，也称目标类，委托类，需要实现接口，上述两步是最基本的项目代码结构；

3. 编写代理类，这里我们想要增强功能，创建一个代理类，并且通过实现接口来与被代理类保持一致；下一步需要注入被代理类的一个实例，用于使用其方法（增强方法，起码需要保留原方法）；接着重写接口定义的方法，将注入的被代理类方法调用，并在重写的方法体内完成增强的操作

### 动态代理被使用的原因

通过上方的叙述，我们了解到静态代理需要编写被代理类的代码来实现代理类的实例化，如果我们需要很多增强功能，就不得不为每一个目标类编写代码，太过于麻烦。除此以外，若接口进行调整，所有的代理类被代理类都需要进行调整，耦合性太高。因此，利用反射来实现动态代理是一种可行的方式。

Java本身就提供了动态代理的方法：在程序的执行过程中，使用JDK的反射机制，创建代理对象，并动态的指定代理的目标类。

### JDK动态代理使用方法

- `Proxy.newProxyInstance(ClassLoader loader, Class<?>[] interfaces, InvocationHandler handler)` 使用该方法直接返回一个**实现相同接口**的代理对象，其中参数为：
  - loader 类加载器，传入被代理类的类加载器
  - interfaces 委托类实现的接口列表，最少传入一个；如果知道接口，则可以使用 `{ MyInterface.class }` 的方式传入，或者使用 `myInstance.getClass().getInterfaces()` 方法获取一个列表（数组）
  - handler 一个调用处理器的实例，这个实例中需要实现的方法 `invoke` 是写增强逻辑的核心部分；注意 `InvocationHandler ` 是一个接口，我们传入的是该接口的实现类

- `InvocationHandler` 重写 `public Object invoke(Object proxy, Method method, Object[] args) {}` 方法即可:

  - proxy为传入的被代理对象，method为该被代理对象的需要增强的方法（这里的被增强的方法实际上也是接口中定义的方法），args就是该方法需要传入的参数，例如：
  
  ```java
  @override
  public Object invoke(Object proxy, Method method, Object[] args) {
      // ...other enhanced functionality 
      Object res = method.invoke(proxy, args)
      // ...other enhanced functionality 
      return res;
  }
  ```

### CGLIB动态代理方法

JDK的问题，如上文所述，通过interface的定义规定委托类以及代理类的行为，但其中如果委托类中存在私有方法（接口未规定的），那么代理类便无法进行代理调用了。因此使用CGLIB（Code Generation Library）机制来解决。

其原理为：原理就是通过字节码技术生成一个子类，并在子类中**拦截**父类方法的调用，织入额外的业务逻辑。这里会使用 **方法拦截器** `MethodInterceptor` 进行拦截。另外需要注意的是，因为使用了继承，因此被 `final` 修饰的类是无法使用该方法的。

使用步骤（需要cglib的依赖，记得引入）：

1. 创建被代理类（委托类）
2. 创建一个方法拦截器实现接口 `MethodInterceptor`，并重写 `intercept(Object var1, Method var2, Object[] var3, MethodProxy var4)` 方法，它 用于拦截并增强委托类的方法（和 JDK 动态代理 `InvocationHandler` 中的 `invoke` 方法类似）,其中：
   - `Object var1` ：委托类对象
   - `Method var2` ：被拦截的方法（委托类中需要被增强的方法）
   - `Object[] var3` ：方法传入的参数列表
   - `MethodProxy var4` ：用于调用委托类的原始方法（底层也是通过反射机制，不过不是 `Method.invoke` 了，而是使用 `MethodProxy.invokeSuper` 方法）
3. 创建代理对象（Proxy）：通过 `Enhancer.create()` 创建委托类对象的代理对象

```java
// 关于增强的逻辑写在实现了MethodInterceptor接口的类中的intercept方法中
@Override
public Object intercept(Object obj, Method method, Object[] args, MethodProxy methodProxy) throws Throwable {
    // ...other enhanced functionality 
    // 通过反射调用委托类的方法
    Object res = methodProxy.invokeSuper(obj, args);
    // ...other enhanced functionality 
    return res;
}

// 创建代理类
Enhancer enhancer = new Enhancer();
// 设置类加载器
enhancer.setClassLoader(clazz.getClassLoader());
// 设置父类（委托类）
enhancer.setSuperclass(clazz);
// 设置方法拦截器（这里传入刚才写好的拦截器实现类即可）
enhancer.setCallback(new MethodInterceptorImpl());
// 生成代理对象，此时生成的obj调用的方法会被增强
MyObject obj = (MyObject) enhancer.create();
```

### 两种方式的对比

1. JDK 动态代理是基于实现了接口的委托类，通过接口实现代理；而 CGLIB 动态代理是基于继承了委托类的子类，通过子类实现代理。

2. JDK 动态代理只能代理实现了接口的类，且只能增强接口中现有的方法；而 CGLIB 可以代理未实现任何接口的类。

3. 就二者的效率来说，大部分情况都是 JDK 动态代理的效率更高，随着 JDK 版本的升级，这个优势更加明显。

### 使用场景

1. 增强前人的代码，利用设计模式的原则“**对修改关闭，对扩展开放**”，使用动态代理增强功能却不破坏其代码；
2. 我们在使用 **RPC 框架**的时候，框架本身并不能提前知道各个业务方要调用哪些接口的哪些方法 。那么这个时候，就可用通过动态代理的方式来建立一个中间人给客户端使用，也方便框架进行搭建逻辑，某种程度上也是客户端代码和框架松耦合的一种表现。（并不是很懂）

3. Spring 中的 AOP 模块中：如果目标对象实现了接口，则默认采用 JDK 动态代理，否则采用 CGLIB 动态代理；



## Java多线程

### 线程基本介绍

两（三）种方法创建一个新线程：

1. 创建一个继承了Thread的实例对象，调用 `start()` 方法，在调用的实例对象内，需要重写 `run()` 方法实现该线程的逻辑；这个方法相当于将**任务**与**线程**合并；

2. 同样创建一个Thread对象，但不同的是，此时创建一个实现了 `Runable` 接口的实例对象，同样重写 `run()` 方法，接着将该对象传入，类似于：

   ` Thread t = new Thread(new MyRunnable());`

   这个方法相当于将**任务**与**线程**分开；

3. 实现 `callable` 接口，利用 `FutureTask` 执行任务

注意，这里也可以使用lambda语法来匿名创建一个实例（或者匿名实现类）；直接调用实例对象中重写的 `run()` 方法会执行其中的逻辑，但不会**创建新的线程**，这相当于简单地调用了一个实例方法，必须使用 `start()` 创建新线程。

**`Thread` 实现任务的局限性**

1. 任务逻辑写在Thread类的run方法中，有单继承的局限性
2. 创建多线程时，每个任务有成员变量时不共享，必须加static才能做到共享

**`Runbale` 相比 `Callable` 有以下的局限性**

1. 任务没有返回值
2. 任务无法抛异常给调用方

#### 设置线程的优先级

`Thread.setPriority(int n)` ：默认值为5，最低为1，最高为10，数字越大优先级越高，对优先级高的线程的调度**可能**更频繁，但不保证**一定会优先调用**；在CPU比较忙的时候，该设置效果最好，调度会更频繁，比较空闲的话，该设置基本无效；

`Thread.yield()` ：礼让，代用该方法的线程会切换到就绪态，这样其他线程的执行机会变高；

#### 守护线程

`thread.setDaemon(true)` ：此方法可以将一个普通线程设置为守护线程

#### 线程状态

- **初始（NEW）：**新创建的线程，尚未执行，即没有调用 `start()` 方法；
- **运行（RUNNABLE）：**运行中的线程，正在执行`run()`方法的Java代码，这里的说法有些不准确，Java线程中将就绪（ready）状态以及运行中（running）状态笼统的成为运行状态（RUNNABLE）；很好理解，就绪状态表示该线程位于可运行线程池（这里的线程池存疑）中，等待被调度；获得了CPU使用权开始工作的线程成为运行中状态；
- **BLOCKED：**运行中的线程，因为某些操作被阻塞而挂起（线程阻塞于锁）；
- **WAITING：**运行中的线程，因为某些操作在等待中（进入该状态的线程需要等待其他线程做出一些特定动作（通知或中断））；这种状态下的线程必须通过**显式**的手段唤醒，不然会**无限期**的等待下去；
- **TIMED_WAITING：**运行中的线程，因为执行`sleep()`方法正在计时等待（不一定只有这个方法，还可能通过其他方法实现，在指定的时间后自行返回）；
- **TERMINATED：**线程已终止，因为`run()`方法执行完毕。

#### 线程阻塞与相关方法

线程的阻塞可以分为好多种，从操作系统层面和java层面阻塞的定义可能不同，但是广义上使得线程阻塞的方式有下面几种：

1. BIO阻塞，即使用了阻塞式的io流
2. sleep(long time) 让线程休眠进入阻塞状态
3. a.join() 调用该方法的线程进入阻塞，等待a线程执行完恢复运行
4. sychronized或ReentrantLock 造成线程未获得锁进入阻塞状态 (同步锁章节细说)
5. 获得锁之后调用wait()方法 也会让线程进入阻塞状态 (同步锁章节细说)
6. LockSupport.park() 让线程进入阻塞状态 (同步锁章节细说)

---

- `thread.join(long time)` ：在某一个线程（主线程）中调用其他线程的 `join()` 方法，会等待该线程执行完毕后（此时主线程转入WAITING状态等待其他线程（子线程）的唤醒，当然传入参数则成为TIMED_WAITING状态），再继续向下执行（主线程）的代码；这里可以传入一个时间参数，超过等待时间后不再等待；若其他线程已经结束，那么会立刻返回（主线程）；
- `Thread.sleep(long millis)` ：静态方法，调用这个方法会让当前线程进入阻塞（TIMED_WAITING）状态，休眠完成后重新争抢CPU时间片

#### 线程的中断

每个线程存在一个中断标记（布尔类型），该标记标识着该线程是否被中断

- `thread.interrupt()`：通过调用此方法对该线程实例发出一个中断请求；注意，仅仅是中断请求，不代表一定会中断；此外，可以在该线程本身使用 `Thread.currentThread().interrupt();` 给自己发送中断请求；
- `thread.isInterrupted()` 获取线程的中断标记 ,调用后不会修改线程的中断标记；该方法用于测试中断标记，并以此为依据执行中断后的逻辑；
- `interrupted()` 获取线程的打断标记，调用后**清空**打断标记，即如果获取为true **调用后**打断标记为**false** (不常用)

>Thread.interrupt()方法不会中断一个正在运行的线程。它的作用是，在线程受到阻塞时抛出一个中断信号，这样线程就得以退出阻塞的状态。更确切的说，如果线程被**Object.wait**,**Thread.join**和**Thread.sleep**三种方法之一阻塞，那么，它将接收到一个中断异常（InterruptedException），从而提早地终结被阻塞状态。

也就是说，如果尝试中断一个正在阻塞的线程，这个线程会抛出一个中断异常（不会将自己标记为被中断），可以在catch块中，处理你的中断逻辑；并且需要注意的是，此时查看中断标记，该标记为**false**；

#### 线程状态转化

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9a8e4857fbc477db432bfddae72e3f2~tplv-k3u1fbpfcp-zoom-1.image)

---

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93f311262656412c83a99b9c03b4815e~tplv-k3u1fbpfcp-zoom-1.image)

#### 线程方法（Thread类）

| 方法名称          | 是否static | 方法说明                                                     |
| ----------------- | ---------- | ------------------------------------------------------------ |
| start()           | 否         | 让线程启动，进入就绪状态,等待cpu分配时间片                   |
| run()             | 否         | 重写Runnable接口的方法,线程获取到cpu时间片时执行的具体逻辑   |
| yield()           | 是         | 线程的礼让，使得获取到cpu时间片的线程进入就绪状态，重新争抢时间片 |
| sleep(time)       | 是         | 线程休眠固定时间，进入阻塞状态，休眠时间完成后重新争抢时间片,休眠可被打断 |
| join()/join(time) | 否         | 调用线程对象的join方法，调用者线程进入阻塞,等待线程对象执行完或者到达指定时间才恢复，重新争抢时间片 |
| isInterrupted()   | 否         | 获取线程的打断标记，true:被打断，false：没有被打断。调用后不会修改打断标记 |
| interrupt()       | 否         | 打断线程，抛出InterruptedException异常的方法均可被打断，但是打断后不会修改打断标记，正常执行的线程被打断后会修改打断标记 |
| interrupted()     | 否         | 获取线程的打断标记。调用后会清空打断标记                     |
| stop()            | 否         | 停止线程运行 不推荐                                          |
| suspend()         | 否         | 挂起线程 不推荐                                              |
| resume()          | 否         | 恢复线程运行 不推荐                                          |
| currentThread()   | 是         | 获取当前线程                                                 |

#### 线程方法（Object类）

| 方法名称                  | 方法说明                               |
| ------------------------- | -------------------------------------- |
| wait()/wait(long timeout) | 获取到锁的线程进入阻塞状态             |
| notify()                  | 随机唤醒被wait()的一个线程             |
| notifyAll();              | 唤醒被wait()的所有线程，重新争抢时间片 |



### 线程与锁

#### 线程通信

`wait()` 以及 `notify()` 方法实现，通过调用 `object.wait()` 方法让线程进入**WAITING**状态（这时，该线程进入Monitor的**WaitSet**中进行等待，该状态也是阻塞状态），释放Object的锁，让其他线程使用；当其中的某一线程使用Object结束后，调用 `object.notify()` 随机唤醒在**WaitSet**中的其中一个线程或者 `object.notifyAll()` 方法唤醒所有线程；

1. 注意，这里的唤醒指的是将其放入 **EntryList** ，之后进行锁的竞争，成功才返回原来的位置继续执行；
2. `wait(time)` 方法可以传入一个时间，到达指定时间后自动返回；
3. `notify()` 方法是一个**无副作用**的方法，可以在另一个线程没有wait的时候调用；
4. `notifyAll()` 在一般情况下比较安全，因为 `notify()` 的使用可能会使一些线程永远Wait下去；
5. 这些方法的使用场景是**必须要有同步**，且**必须获得对象的锁**才能调用,使用锁对象去调用,否则会抛异常；此外，`notify()` 以及 `notifyAll()` 都不是**立刻释放锁**的，直到完成该线程的临界区任务才会释放锁；

#### 可重入锁 ReentrantLock

可重入锁表示对于一个线程与一把锁，如果在不释放的前提下可以加同一把锁，这种锁类型被称为可重入锁；Synchronized是隐式的可重入锁；

```java
// 与Synchronized关键字不同，需要显式定义可重入锁
private final Lock lock = new ReentrantLock();

// 使用方式为，利用try...finally进行操作
lock.lock();
try {
    ...Operations
} finally {
    lock.unlock();
}
```

##### 锁的基本方法：

1. `void lock()`：加锁，若被占用就进入等待状态（和一般锁一致）
2. `boolean tryLock(long timeout, TimeUnit unit)`：比较关键的一个方法，尝试加锁，并且设置一个等待时间，一段时间后没有获取到锁，可以选择直接放弃并释放所有占用资源。该方法破坏了死锁条件，因此不会出现死锁；另外，因为是自己编写处理逻辑，可以在该层面上实现“自旋”，也可以处理中断异常，在 `catch`中回收资源；
3. `void unlock()`：释放锁，与 `lock()` 对应；
4. `boolean tryLock()`：不带参数，意味着不能获得锁就返回false；

##### 可重入锁的通信方式

```java
private final Lock lock = new ReentrantLock();
// 使用Condition进行通信，注意，需要有lock实例才可以
private final Condition condition = lock.newCondition();
```

`Condition` 提供的 `await()`、`signal()`、`signalAll() `原理和 `synchronized` 锁对象的 `wait()`、`notify()`、`notifyAll()` 是一致的，并且其行为也是一样的：

- `await()`：会释放当前锁，进入等待状态；（ `condition.await(1, TimeUnit.SECOND)` 可以设置时间，这一点与 `wait()` 也相同）；
- `signal()`：会唤醒某个等待线程；
- `signalAll()`：会唤醒所有等待线程；
- 唤醒线程从`await()`：返回后需要重新获得锁。

##### 可重入锁优点

1. 支持获取锁的超时时间，这体现在 `tryLock()` 中
2. 获取锁时可被打断， 同理，因为是“tryLock”，尝试获取
3. 可设为公平锁，构造器可传入是否设置公平性的布尔值
4. 可以有不同的条件变量，即有多个waitSet，可以指定唤醒，不同于Object的通知方法，这里是对同一把锁构造不同的条件 `Condition`，然后通过这些条件去唤醒不同的线程，而不是随机唤醒

#### Java内存模型 JMM

JMM的特点体现在以下三点：

1. 原子性 保证指令不会受到上下文切换的影响
2. 可见性 保证指令不会受到cpu缓存的影响
3. 有序性 保证指令不会受并行优化的影响

##### 可见性

可见性指每个线程的缓存，保存了共享变量时，是否能够**察觉**到该变量的改动；若主线程改变了一般的静态变量，其他线程无法收到该变量的改动消息；

> **注意：**JVM在运行时，每个线程都会在自己的工作空间（**CPU高速缓存**保存的副本，不是**栈区**）保存一份变量的副本（如果变量共享）

##### 有序性

JVM可能会打乱指令的排序，来达到和预期相同的效果，这是JVM的优化；重排序必须满足一个条件（as-if-serial 原则），就是在单线程的环境下，重排序执行结果与排序前相同；优化的方面并不是指性能，而是提升CPU的利用率

##### 原子性

共享的变量是否能够在同一时间内被同一个线程操作和修改是原子性的关键；

#### Volatile

从规则的定义可知，如果多个线程同时操作volatile变量，那么对该变量的**写操作**必须在**读操作**之前执行(禁止重排序)，并且**写操作**的结果对**读操作可见**（强缓存一致性）。`volatile` 关键字定义的共享变量在修改后立马就会暴露给其他CPU，并且能保证在读取volatile定义的共享变量一定是当前最新的数据，能保证最新数据的原因是：该指令通过**内存屏障**的方式解决了指令重排（有序性）以及可见性的问题，而内存屏障的机制是为了解决ESMI协议（一种缓存锁）的弱一致性问题，这个协议中需要用到store buffer暂时存放指令的数据的操作结果，当然，为了使这个空间尽量大，**失效队列**被使用，详情看这篇知乎文章：[深入理解volatile](https://zhuanlan.zhihu.com/p/397640787)；内存屏障包括下面三种

**Store Barrier(写屏障)**

强制所有在store屏障指令之前的store指令，都在该store屏障指令执行之前被执行，并把store缓冲区的数据都刷到CPU缓存。

结合上面的场景，这个指令其实就是告诉CPU，执行这个指令的时候需要把store buffer的数据都同步到内存中去。

**Load Barrier(读屏障)**

强制所有在load屏障指令之后的load指令，都在该load屏障指令执行之后被执行，并且一直等到load缓冲区被该CPU读完才能执行之后的load指令。

这个指令的意思是，在读取共享变量的指令前，先处理所有在失效队列中的消息，这样就保证了在读取数据之前所有失效的消息都得到了执行，从而保证自己是读取到的树是最新的。

**Full Barrier（全能屏障）**

包含了Store Barrier 和Load Barrier的功能。

#### CAS

CAS是Compare and Swap的缩写，是一种自旋锁，这在源码中有体现，他会比较提交修改时对比旧值E，也成预期值（最开始从内存中读到的值）与内存中当前值V是否相同，若相同证明没有其他线程对其修改，此时将值设置为操作后的新值N，若不同，证明已被修改，此时自旋，重新读值重新操作，直到成功；

**乐观锁**

综上，我们可以知道CAS是一种乐观锁的形式，当没有太多竞争时，自旋次数较少，这种操作底层是**Native**方法，我们只需要知道该操作是原子性的，不可分割，因此代价较小（相较于synchronized）；但是在竞争激烈的环境下，自旋这种消耗系统资源的方式肯定是开销较大的，相较于悲观锁；

**Java中的应用**

CAS运用在原子类上，例如

1. AtomicInteger/AtomicBoolean/AtomicLong
2. AtomicIntegerArray/AtomicLongArray/AtomicReferenceArray
3. AtomicReference/AtomicStampedReference/AtomicMarkableReference

**ABA问题**

不知道这个问题会带来什么后果，就是说原本值为A，被一个线程改成B，但又被另一个线程改为A，让第一个线程认为没有发生改变；这个问题的解决方案是使用标记或者版本号的方式解决，例如上方的两个类；

### 线程池

#### 优势

1. 降低资源消耗，通过池化思想，减少创建线程和销毁线程的消耗，控制资源
2. 提高响应速度，任务到达时，无需创建线程即可运行
3. 提供更多更强大的功能，可扩展性高

#### 构造器

```java
public ThreadPoolExecutor(
    int corePoolSize, // 线程池核心线程数量
    int maximumPoolSize, // 线程池最大线程数量
    long keepAliveTime, // 救急线程空闲时间
    TimeUnit unit, // 空闲时间单位
    BlockingQueue<Runnable> workQueue, // 阻塞队列
    ThreadFactory threadFactory,  // 创建线程的工厂，主要用来定义线程名
    RejectedExecutionHandler handler) {} // 拒绝策略处理器
```

其中，空闲时间指，非核心线程在一定时间内没有接收到任务会被回收（~~此处暂时不明白是销毁还是就设置一个标记使其撤销~~）；根据理解，是销毁线程；

#### 线程池状态

注意，是**线程池**整体的状态，线程池通过int变量存储“整体状态”，其中高三位表示线程池状态，后29位表示线程池的整体数量；

```java
// runState is stored in the high-order bits
private static final int RUNNING    = -1 << COUNT_BITS;
private static final int SHUTDOWN   =  0 << COUNT_BITS;
private static final int STOP       =  1 << COUNT_BITS;
private static final int TIDYING    =  2 << COUNT_BITS;
private static final int TERMINATED =  3 << COUNT_BITS;
```

---

| 状态名称  | 高三位 | 接收新任务 | 处理阻塞队列任务 | 说明                                                         |
| --------- | ------ | ---------- | ---------------- | ------------------------------------------------------------ |
| Running   | 111    | Y          | Y                | 正常接收任务，正常处理任务                                   |
| Shutdown  | 000    | N          | Y                | 不会接收任务,会执行完正在执行的任务,也会处理阻塞队列里的任务 |
| Stop      | 001    | N          | N                | 不会接收任务，会中断正在执行的任务,会放弃处理阻塞队列里的任务 |
| Tidying   | 010    | N          | N                | 任务全部执行完毕，当前活动线程是0，即将进入终结              |
| Termitted | 011    | N          | N                | 终结状态                                                     |

很好理解的状态，正常情况下就是**Running**，当处理线程数等于最大线程数转为**Shutdown**状态

#### 运行逻辑

1. 创建，设定初始化参数创建线程池实例后，进入**Running**状态；
2. 提交任务，此时线程池创建线程处理任务；
3. 当池内工作线程数超过了**corePoolSize**时，再提交任务会将任务放进阻塞队列**workQueue**；
4. 当阻塞队列装满后，再提交任务，线程池会创建救急线程来处理任务；（此时不清楚这个地方的新任务放在哪）；
5. 此时当池内工作线程数超过**maximumPoolSize**，再提交任务，线程池会执行拒绝策略；
6. 当线程取任务的时间达到keepAliveTime还没有取到任务，工作线程数大于corePoolSize时，会回收该线程（线程池内的线程都是平等的，不会说先创建的就是核心线程，这里指的是空闲出来的时间）；

#### 拒绝策略

有下列的拒绝策略可供选择：

1. `AbortPolicy` (默认策略)：调用者**直接**抛出RejectedExecutionException 
2. `CallerRunsPolicy` ：让调用者所在的线程运行任务
3. `DiscardPolicy` ：丢弃此次任务
4. `DiscardOldestPolicy`：丢弃阻塞队列中最早的任务，加入该任务

#### 阻塞队列的种类

1. `ArrayBlockingQueue`

   - 根据类名称，这是一个由数组实现的阻塞队列，FIFO；

2. `LinkedBlockingQueue`

   - 根据类名称，这是一个由链表实现的阻塞队列，FIFO；

   - 吞吐量通常要高于 `ArrayBlockingQueue`，我想是因为链表插入删除效率比较高；

   - `fixedThreadPool` 使用的阻塞队列为该队列；

   - 无界队列，可以无限扩充；

3. `SynchronousQueue`

   - 没有存储空间的阻塞队列，任务提交给该队列后必须要交给一条工作线程处理；如果当前没有空闲的工作线程，则立即创建一条新的工作线程；
   - `cachedThreadPool` 用的阻塞队列为该队列；
   - 无界队列，可以无限扩充；

4. `PriorityBlockingQueue`

   - 优先权阻塞队列；没啥理解，可能比较像优先队列吧，那么数据结构可能会有一定不同；

#### 提交任务

可以向 `ThreadPoolExecutor` 提交两种任务：`Callable` 和 `Runnable`：

1. `Callable`：该类任务有返回结果，可以抛出异常；通过 `submit()` 函数提交，返回 `Future` 对象；可通过`get` 获取执行结果；该类任务适用于**需要返回值结果**的任务；
2. `Runnable`：该类任务只执行，无法获取返回结果，并在执行过程中无法抛异常；通过execute提交。

使用 `threadPool.submit(new myTask());` 提交任务

#### 创建线程池的方法

这里的方法同一为 `Executors.newPool()` 格式

1. **newFixedThreadPool**

```java
public static ExecutorService newFixedThreadPool(int nThreads) {
    return new ThreadPoolExecutor(nThreads, nThreads,
                                  0L, TimeUnit.MILLISECONDS,
                                  new LinkedBlockingQueue<Runnable>());
}
```

- 根据参数看到，是**固定的**核心线程数以及最大线程数，**没有救急线程**；

- 阻塞队列是一个无界的队列，**永远不会拒绝新任务**，因此可能会导致OOM；

---

​	2.**newCachedThreadPool**

```haxe
public static ExecutorService newCachedThreadPool() {
    return new ThreadPoolExecutor(0, Integer.MAX_VALUE,
                                  60L, TimeUnit.SECONDS,
                                  new SynchronousQueue<Runnable>());
}
```

- 根据参数，没有限制的最大线程数量，核心线程为0；
- 适合处理执行时间比较小的任务
- 阻塞队列是一个没有容量的同步队列，意味着可以不断接受任务，但必须**一直有线程**来取任务，这个线程池的策略就是**无限的生成线程**，可能导致线程过多，CPU负担过重；

---

​	3.**newSingleThreadExecutor**

```haxe
public static ExecutorService newSingleThreadExecutor() {
    return new FinalizableDelegatedExecutorService
        (new ThreadPoolExecutor(1, 1,
                                0L, TimeUnit.MILLISECONDS,
                                new LinkedBlockingQueue<Runnable>()));
}
```

- 可以看出这是一个**串行化**执行的线程池，核心线程数只有1，并且阻塞队列无限，因此**不会创建救急线程**；
- 核心线程数和最大线程数都是1，没有救急线程，无界队列 可以不停的接收任务，可能造成OOM；
- 将任务串行化 一个个执行， 使用包装类是为了屏蔽修改线程池的一些参数 比如 corePoolSize；
- 如果某线程抛出异常了，会重新创建一个线程继续执行；

---

​	4.**newScheduledThreadPool**

```haxe
public static ScheduledExecutorService newScheduledThreadPool(int corePoolSize) {
    return new ScheduledThreadPoolExecutor(corePoolSize);
}

// 使用方法略有不同，下面是例子:
ScheduledExecutorService ses = Executors.newScheduledThreadPool(4);
// 1秒后执行一次性任务:
ses.schedule(new Task("one-time"), 1, TimeUnit.SECONDS);
// 2秒后开始执行定时任务，每3秒执行1次:
ses.scheduleAtFixedRate(new Task("fixed-rate"), 2, 3, TimeUnit.SECONDS);
// 2秒后开始执行定时任务，以3秒为间隔执行:
ses.scheduleWithFixedDelay(new Task("fixed-delay"), 2, 3, TimeUnit.SECONDS);
```

- 适合于**周期性**（隔一段时间调用）的任务，或者需要**定时**（延迟指定时间后调用）的任务；
- 任务调度的线程池 可以指定延迟时间调用，可以指定隔一段时间调用；
- 注意，`FixedRate` 表示每次任务的**执行时间**都是一个固定值，`Delay` 表示每次任务之间**间隔**（相当于空闲时间）都是一个固定值；
- 一种特殊情况是 `FixedRate` 中，上一个任务在固定执行时间区域内**未完成任务**，下一个任务**不会并发执行**，而是等待此任务**结束后立刻开始**，如果上一个任务**抛出异常**，下一个任务**不会执行**；

#### 线程池关闭

- `shutdown()` ：优雅关闭，根据上方线程池状态可以看出，该状态会拒绝接受新任务，但会完成工作中的任务以及阻塞队列中的任务，然后关闭；
- `shutdownNow()` ：将线程池状态设置为Stop，不能接收任务，会立即中断执行中的工作线程，并且不会执行阻塞队列里的任务， 会返回阻塞队列的任务列表；
- `awaitTermination(timeout, unit)` ：指定时间以及时间单位后，观测线程池状态，一般与 `shutdown()` 配合使用，观测是否关闭，或者进行定时关闭；

#### 配置与使用

|   |  cpu密集型     |                    io密集型         |
| ---------- | --------------- | ------------------------- |
| 线程数数量 | 核数<=x<=核数*2（可以设置为CPU数量+1） | 核心数*50<=x<=核心数* 100 |
| 队列长度   | y>=100          | 1<=y<=10                  |

拒绝策略可以参考Tomcat的拒绝策略，例如捕获到异常后额外尝试一次，再捕获不到则抛出真正的异常
