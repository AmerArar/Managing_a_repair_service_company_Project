import Main
def test():
     assert Main.TreatmentTimeForFaultType('Critical malfunction') == "2", "Should be 2"
     assert Main.TreatmentTimeForFaultType('Normal malfunction') == "1", "Should be 1"
     assert Main.TreatmentTimeForFaultType('Maintenance failure') == "0.5", "Should be 0.5"

     assert Main.returnLocationByclientPhone('0508327494')=="TAL SHEVA", "Should be returned TAL SHEVA"

     assert Main.DistanceKmInHours('23.5')==0.7833333333333333, "Should be returned 0.7833333333333333"
     assert Main.strToInt("1234")==1234, "Should be returned 1234"
     assert Main.strToInt("1234.9")==1234.9, "Should be returned 1234.9"
     print("Everything passed")
test()
