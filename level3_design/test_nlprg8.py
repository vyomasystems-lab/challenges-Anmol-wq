import os
import random
# from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_nlprg8(dut):

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)

        for i in range(7):
        
            in0 = random.randint(0, 1)
            in1 = random.randint(0, 1)
            in2 = random.randint(0, 1)
            in3 = random.randint(0, 1)
            in4 = random.randint(0, 1)
            in5 = random.randint(0, 1)
            in6 = random.randint(0, 1)
            in7 = random.randint(0, 1)

            input=[in0,in1,in2,in3,in4,in5,in6,in7]

            dut.o0.value = in0
            dut.o1.value = in1
            dut.o2.value = in2
            dut.o3.value = in3
            dut.o4.value = in4
            dut.o5.value = in5
            dut.o6.value = in6
            dut.o7.value = in7

            dut._log.info(f' DUT={dut.o[i].value}')
            assert dut.o[i].value==input[i]
            

