# ConsoleRenderer
_Best type of learning is learning by doing_ SIMEA

           ____      ____      __      __     ______       ____      __        _______       
          /    |    /    \    |   \   |  |   /      |     /    \    |  |      |       |      
         /   __|   /      \   |    \  |  |  |   ____|    /      \   |  |      |   ____|      
        |   |     |   /\   |  |  \  \ |  |  |  |_____   |   /\   |  |  |      |  |__         
        |   |     |  |  |  |  |  |\  \|  |   \_____  \  |  |  |  |  |  |      |   __|        
        |   |__   |   \/   |  |  | \  \  |   _____|  |  |   \/   |  |  |____  |  |____       
         \     |   \      /   |  |  \    |  |        |   \      /   |       | |       |      
          \____|    \____/    |__|   \___|  |_______/     \____/    |_______| |_______|      
       _____     _______   __      __    ______     _______    _____     _______   _____     
      |     \   |       | |   \   |  |  |      \   |       |  |     \   |       | |     \    
      |  |\  |  |   ____| |    \  |  |  |   _   \  |   ____|  |  |\  |  |   ____| |  |\  |   
      |  |/  |  |  |__    |  \  \ |  |  |  | \   | |  |__     |  |/  |  |  |__    |  |/  |   
      |     /   |   __|   |  |\  \|  |  |  |  |  | |   __|    |     /   |   __|   |     /    
      |  |  \   |  |____  |  | \  \  |  |  |_/   | |  |____   |  |  \   |  |____  |  |  \    
      |  |\  \  |       | |  |  \    |  |       /  |       |  |  |\  \  |       | |  |\  \   
      |__| \__\ |_______| |__|   \___|  |______/   |_______|  |__| \__\ |_______| |__| \__\  
   
## Short description
Program here renders 3D object with ASCII characters as pixels. Its early alpha still.

## TODO list
- input during program is running, for configuration things like:
  - switching between two types of render created
  - switching between "materials"(specific ASCII characters), and light-like visuals
  - switching on and off debug logs
  - enabling dynamic loading obj files(simple 3D mesh data)
  - dynamic renderer resize
- new renderer add optimization for triangles intersecting with camera being rendered(now it's a bug)
- remove problem with "inverse movement"
- add info about input
- add possibility for rotating the camera around other axes

## Known bugs
- triangles intersecting with camera are unoptimized and renders artifacts,
- backface culling is off

## Input
- 'w','s','a','d' for horizontal movement, 'q' and 'e' for vertical movement, 'j' and 'l' for rotating the camera

![view sample](https://github.com/palemek/ConsoleRenderer/blob/master/gif.gif "view sample")
