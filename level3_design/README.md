# Final report: Sudhanshu Singh(level3_design)
Value are initialised with

![image](https://user-images.githubusercontent.com/73732594/182122086-6417533d-2cc0-4113-951a-2e5c7a0b64ef.png)



The assertion error seen for one set of random input

![image](https://user-images.githubusercontent.com/73732594/182122316-3b485955-d7c9-42a2-81df-d23f8e7bebdc.png)


# Test Scenerio
 
*Expected output after one clock pulse: 001

*Observed output in dut.out.value: 000 

 Output mismatched with expected output proving there is a design bug



# Design Bug
 Based on above test input and analysing the design we see following

![image](https://user-images.githubusercontent.com/73732594/182123590-57a3efb9-ebb1-446b-b513-e3ac5dba2c0c.png)


For the design, at the place of 'assign o[0] = o1' it should be 'assign o[0] = o0'

# Design Fix

Updating the design and rerunning the test the test pass

![image](https://user-images.githubusercontent.com/73732594/182123907-d43d3dce-5f83-4c79-9a87-8383c6e4a4d3.png)


