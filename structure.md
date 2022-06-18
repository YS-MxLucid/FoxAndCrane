Core

| 元件               | 功能                               | 备注 |
| :----------------- | ---------------------------------- | ---- |
| Performer          | 组织并依次展现渲染完毕的Screen     |      |
| Recorder           | 存读档系统（写入读出 Status/Data） |      |
| Computer           | 演算游戏数据以推动事件             |      |
| Status Structure   | 游戏状态数据结构                   |      |
| Database Structure | 游戏素材数据结构                   |      |
| 4th Wall           | 与玩家和系统的交互                 |      |

Renderer

| 元件             | 功能                           | 备注 |
| ---------------- | ------------------------------ | ---- |
| Text Renderer    | 对文字的前处理和渲染           |      |
| Image Renderer   | 对图像的前处理和渲染           |      |
| Element Renderer | 对界面要件的排版和渲染         |      |
| Screen Renderer  | 对界面的组合和渲染，返回Screen |      |



Game Structure:

* Game Object
  * Scenario剧本 *【由Screen构成的序列】
    * Screen界面 * 【由Element构成的界面】
      
      > Screen当中应当包含：1. Element列表；
      
      * Element要件 * 【文字和图片构成的简单可复用界面要件】
      
        > Element本身的结构应当分为以下部分，1. 组分的字典，每个组分名对应着其所有变体构成的列表；2. 组分与游戏变量的对应，也就是游戏变量决定该显示哪一个变体；3. 显示这个Element可选择的所有组织样式（特别的，Invisible也是一种格式）；4. Element内部Component的层级关系； 5. Element自身的位置、角度， etc； 6. 经由Element生成的在当前状态下的Surface
      
        * Component元素 * 【要件的组成文字和图片，应该都是一个基础surface类别中的元素】
        
          > 存储在Database中，理论上是无格式的，由Element的属性决定其格式
      
    * Event Tree事件树 * 【一个树状结构，根据游戏变量决定可以进入哪个界面】
  
  * Variable变量 * 【保存所有的游戏变量】
  
    * StatusVar * 【进入存档数据的状态变量】
    * RunTimeVar * 【单次运行中有效的临时变量】
  
  * Database * 【保存素材数据的数据库】
  
    > 可以用数据库的方式存储而不必读入内存之中 （比如HDF5格式？）