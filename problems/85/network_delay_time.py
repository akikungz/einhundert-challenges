def network_delay_time(times: list, N: int, K: int) -> int:
    pass

def main():
    times = [(2, 1, 1), (2, 3, 1), (3, 4, 1)]
    N = 4
    K = 2
    
    print(network_delay_time(times, N, K))  # 2
    
    times = [(1, 2, 1), (2, 3, 2), (1, 3, 4)]
    N = 3
    K = 1
    
    print(network_delay_time(times, N, K))  # 3
    
    times =  [(1, 2, 1),(1, 3, 2),(2, 4, 1),(3, 4, 2), (4, 5, 1), (5, 6, 2), (1, 6, 4)]
    N = 6
    K = 1
    
    print(network_delay_time(times, N, K))  # 4
    
if __name__ == "__main__":
    main()
