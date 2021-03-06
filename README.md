# Python-Algorithms

A group of different python files with different uses.

## Recursive functions

Functions that fill a matrix in a certain way.

### Cube pattern

Fill a cube in 3 different ways, one method for each face of the cube. 

#### Example

```
Digita un numero entero impar n:3
Caso 1:
[[[ 1.  8.  7.]
  [ 2.  9.  6.]
  [ 3.  4.  5.]]

 [[10. 17. 16.]
  [11. 18. 15.]
  [12. 13. 14.]]

 [[19. 26. 25.]
  [20. 27. 24.]
  [21. 22. 23.]]]



Caso 2:
[[[ 1. 10. 19.]
  [ 2. 11. 20.]
  [ 3. 12. 21.]]

 [[ 8. 17. 26.]
  [ 9. 18. 27.]
  [ 4. 13. 22.]]

 [[ 7. 16. 25.]
  [ 6. 15. 24.]
  [ 5. 14. 23.]]]



Caso 3:
[[[ 1.  8.  7.]
  [10. 17. 16.]
  [19. 26. 25.]]

 [[ 2.  9.  6.]
  [11. 18. 15.]
  [20. 27. 24.]]

 [[ 3.  4.  5.]
  [12. 13. 14.]
  [21. 22. 23.]]]
```
### Diamond pattern

Fill a matrix with a diamond shape and puts numbers in certain way.

#### Example
```
Digita un numero entero impar n:9
                   1
               2  26  10
           3  30   9  27  11
       4  34   8  31  12  28  20
   5  38   7  35  13  32  19  29  21
       6  39  14  36  18  33  22
          15  40  17  37  23
              16  41  24
                  25
```

### Home pattern

Fill a matrix with a house shape and puts numbers in certain way.

#### Example
```
Digite número entero impar de columnas :9
Digite número entero de filas superior a 5:9
                   1
               2   3   4
           5   6   7   8   9
      10  11  12  13  14  15  16
  17  18  19  20  21  22  23  24  25
  26  27  28  29  30  31  32  33  34
  35  36  37  38  39  40  41  42  43
  44  45  46  47  48  49  50  51  52
  53  54  55  56  57  58  59  60  61
```
### Home pattern v2

Fill a matrix with a house shape and puts numbers in certain way.

#### Example
```
digite un numero impar:9
                   5
               6  22   4
           7  21  37  23   3
       8  20  38  50  36  24   2
   9  19  39  49  61  51  35  25   1
  60  59  58  57  56  55  54  53  52
  40  41  42  43  44  45  46  47  48
  34  33  32  31  30  29  28  27  26
  10  11  12  13  14  15  16  17  18
```

### Square pattern

Fill a matrix with a square shape and puts numbers in certain way.

#### Example
```
digite un numero:10
   1  56  57  59  61  64  67  71  75  80
   2   3  58  60  63  66  70  74  79  84
   4   5   7  62  65  69  73  78  83  88
   6   8  10  13  68  72  77  82  87  91
   9  11  14  17  21  76  81  86  90  94
  12  15  18  22  26  31  85  89  93  96
  16  19  23  27  32  36  40  92  95  98
  20  24  28  33  37  41  44  47  97  99
  25  29  34  38  42  45  48  50  52 100
  30  35  39  43  46  49  51  53  54  55
```

### Triangle pattern

Fill a matrix with a triangle shape and puts numbers in certain way.

#### Example
```
Digita un numero entero par n:10
                                       1
                                  20   2
                              21  37   3
                          22  52  38   4
                      23  53  65  39   5
                  24  54  76  66  40   6
              25  55  77  85  67  41   7
          26  56  78  92  86  68  42   8
      27  57  79  93  97  87  69  43   9
  28  58  80  94 100  98  88  70  44  10
      29  59  81  95  99  89  71  45  11
          30  60  82  96  90  72  46  12
              31  61  83  91  73  47  13
                  32  62  84  74  48  14
                      33  63  75  49  15
                          34  64  50  16
                              35  51  17
                                  36  18
                                      19
```

### Z pattern

Fill a matrix with a square shape and puts numbers in certain way that resembles the letter Z.

#### Example
```
Digite número entero: 10
  37  38  39  40  41  42  43  44  45  46
  36  16  17  18  19  20  21  22  47  72
  35  15   4   5   6   7  23  48  73  71
  34  14   3   1   8  24  49  74  90  70
  33  13   2   9  25  50  75  91  89  69
  32  12  10  26  51  76  92  99  88  68
  31  11  27  52  77  93 100  98  87  67
  30  28  53  78  94  95  96  97  86  66
  29  54  79  80  81  82  83  84  85  65
  55  56  57  58  59  60  61  62  63  64



  55  29  30  31  32  33  34  35  36  37
  56  54  28  11  12  13  14  15  16  38
  57  79  53  27  10   2   3   4  17  39
  58  80  78  52  26   9   1   5  18  40
  59  81  94  77  76  51   8   6  19  41
  60  82  95  93  50  25  24   7  20  42
  61  83  96 100  92  75  49  23  21  43
  62  84  97  98  99  91  74  48  22  44
  63  85  86  87  88  89  90  73  47  45
  64  65  66  67  68  69  70  71  72  46
```

### Z diamond pattern

Fill a matrix with a diamond shape and puts numbers in certain way that interchange numbers between "columns".

#### Example
```
Digita un numero entero n:9
                   1
               2  17   3
           4  18  29  19   5
       6  20  30  37  31  21   7
   8  22  32  38  41  39  33  23   9
      10  24  34  40  35  25  11
          12  26  36  27  13
              14  28  15
                  16
```

## Networks functions 

Different functions vinculated to networks and how they work.


## Author

**Camilo Sinning** - [CamiloSinningUN](https://github.com/CamiloSinningUN)
