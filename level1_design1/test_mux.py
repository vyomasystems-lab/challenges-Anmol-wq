# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')

      sel=5'b01101
      inp12=2'b11
      inp13=2'b01

      dut.sel.value = sel
      await Timer(1, units="ns")
      dut.inp12.value = inp12
      await Timer(1, units="ns")
      dut.inp13.value = inp13
      await Timer(1, units="ns")
      dut.inp12.value = inp12
      await Timer(1, units="ns")
      dut._log.info("my out is %s", dut.out.value)
      assert dut.out.value == dut.inp12.value, "could be sel13 because same sel bits assigned for both"
      assert dut.out.value == dut.inp13.value, "could be sel12 because same sel bits assigned for both"


      

      
    
