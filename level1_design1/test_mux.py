# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')

    

    dut.sel.value = 13
    await Timer(1, units="ns")
    dut.inp12.value = 2
    await Timer(1, units="ns")
    dut.inp13.value = 3
    await Timer(1, units="ns")
    dut.inp12.value = 0
    await Timer(1, units="ns")
    dut._log.info("my out is %s", dut.out.value)
    assert dut.out.value == dut.inp12.value, "could be sel13 because same sel bits assigned for both"
    assert dut.out.value == dut.inp13.value, "could be sel12 because same sel bits assigned for both"


      

      
    
