\ Model beckFiala
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
 [ 2 x0 ^2 + 2 x1 ^2 + 2 x2 ^2 + 2 x3 ^2 + 2 x4 ^2 ] / 2 
Subject To
 D0: x0 + x2 + x3 = 0
 D1: x2 + x4 = 0
 D2: x3 + x4 = 0
Bounds
 -100 <= x0 <= 100
 -100 <= x1 <= 100
 -100 <= x2 <= 100
 -100 <= x3 <= 100
 -100 <= x4 <= 100
End
