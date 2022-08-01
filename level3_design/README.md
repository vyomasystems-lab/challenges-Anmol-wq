# Final report: Sudhanshu Singh(level3_design)
Value are initialised with

![image](https://user-images.githubusercontent.com/73732594/182122086-6417533d-2cc0-4113-951a-2e5c7a0b64ef.png)



The assertion error seen for one set of random input

![image](https://user-images.githubusercontent.com/73732594/182122316-3b485955-d7c9-42a2-81df-d23f8e7bebdc.png)


# Test Scenerio
 
*Expected output after one clock pulse: 001

*Observed output in dut.out.value: 000 

 Output mismatched with expected output proving there is a design bug

![image](https://user-images.githubusercontent.com/73732594/182030023-4df5be1d-bd32-44aa-b649-1c4d7394114e.png)

# Design Bug
 Based on above test input and analysing the design we see following

![image](https://user-images.githubusercontent.com/73732594/182030468-80aee04b-059b-49ca-ac1e-98a32f2bb297.png)

For the design, at the place of 5'b01101: out = inp12, it should be 5'b01100: out = inp12

# Design Fix

Updating the design and rerunning the test the test pass

![image](https://user-images.githubusercontent.com/73732594/182030715-97feee16-f489-4ac2-9d2f-1162e4663ac1.png)

