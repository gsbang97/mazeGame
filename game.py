import makeMap,makeTurtle, makeRoad

map = makeMap.makeMap()
road, rego = makeRoad.makeRoad(map)
makeTurtle.makeTurtle(20,road,rego,map)