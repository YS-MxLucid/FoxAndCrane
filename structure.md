Core

| Component          | Function                           | Further Note |
| :----------------- | ---------------------------------- | ------------ |
| Performer          | 组织并依次展现渲染完毕的Screen     |              |
| Recorder           | 存读档系统（写入读出 Status/Data） |              |
| Computer           | 演算游戏数据以推动事件             |              |
| Status Structure   | 游戏状态数据结构                   |              |
| Database Structure | 游戏素材数据结构                   |              |
| 4th Wall           | 与玩家和系统的交互                 |              |

Renderer

| Component        | Function                       | Further Note |
| ---------------- | ------------------------------ | ------------ |
| Text Renderer    | 对文字的前处理和渲染           |              |
| Image Renderer   | 对图像的前处理和渲染           |              |
| Element Renderer | 对界面要件的排版和渲染         |              |
| Screen Renderer  | 对界面的组合和渲染，返回Screen |              |



Game Structure:

* Game Object
  * Scenes *【由Screen构成的序列】
    * Screen * 【由Element构成的界面】
      * Elements * 【文字和图片构成的简单可复用界面要件】
      * Screen Variants * 【同一界面的变体，即随着游戏变量的改变，这个界面上的一部分要件会发生变化，Variant仅记录变动而不记录共有的部分】
    * Event Tree * 【一个树状结构，根据游戏变量决定可以进入哪个界面】
  * Database * 【保存素材数据的数据库，大约有个地址就可以】