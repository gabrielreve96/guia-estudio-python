class Strategy:
    def execute(self, data):
        pass

class StrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class StrategyB(Strategy):
    def execute(self, data):
        return reversed(sorted(data))

# Uso del patrón Strategy
data = [5, 3, 8, 1, 7]

strategy_a = StrategyA()
result_a = strategy_a.execute(data)
print("Estrategia A:", result_a)  # Output: [1, 3, 5, 7, 8]

strategy_b = StrategyB()
result_b = strategy_b.execute(data)
print("Estrategia B:", list(result_b))  # Output: [8, 7, 5, 3, 1]
