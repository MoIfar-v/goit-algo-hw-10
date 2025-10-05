import timeit


def find_coins_greedy(amount, coins):
    result = {}
    remaining = amount
    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            result[coin] = count
            remaining -= coin * count

        if remaining == 0:
            break

    return result



def find_min_coins(amount, coins):
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    # відновлюємо словник результату
    result = {}
    remaining = amount
    while remaining > 0:
        coin = last_coin[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return dict(sorted(result.items()))

if __name__ == "__main__":
    try:
        limit = int(input("Введіть сумму (наприклад 137): "))
    except Exception:
        limit = 137
    
    coins_set = [50, 25, 10, 5, 2, 1]
    
    greedy_time = timeit.timeit(lambda: find_coins_greedy(limit, coins_set), number=1000)
    dp_time = timeit.timeit(lambda: find_min_coins(limit, coins_set), number=1000)

    greedy_result = find_coins_greedy(limit, coins_set)
    dp_result = find_min_coins(limit, coins_set)

    print("\n=== Жадібний алгоритм ===")
    print(greedy_result)
    print(f"Середній час виконання (1000 запусків): {greedy_time:.8f} сек")

    print("\n=== Алгоритм динамічного програмування ===")
    print(dp_result)
    print(f"Середній час виконання (1000 запусків): {dp_time:.8f} сек")

    print("\n=== Порівняння ===")
    print(f"Жадібний алгоритм: {greedy_time:.8f} сек")
    print(f"Динамічний алгоритм: {dp_time:.8f} сек")

    if greedy_time < dp_time:
        print("➡ Жадібний алгоритм швидший, але може бути не оптимальним у загальному випадку.")
    else:
        print("➡ Динамічне програмування повільніше, але завжди гарантує мінімальну кількість монет.")