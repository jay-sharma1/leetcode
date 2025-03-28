def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    currentPos = position.sort()
    
    # Positions of vehicles AFTER the've advanced in speed once.
    futurePos = [currentPos[i] + speed[i] for i in range(len(currentPos))]
    
    # A fleet is formed if two vehic
    