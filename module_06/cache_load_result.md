# Tests without cache
## 60-1-1
Running 1m test @ http://localhost:8081/ \
1 threads and 1 connections \
Thread Stats   Avg      Stdev     Max   +/- Stdev \
Latency     3.63ms    1.06ms  27.46ms   98.71% \
Req/Sec   279.00     16.59   303.00     80.33% \
Latency Distribution \
50%    3.51ms \
75%    3.70ms \
90%    3.93ms \
99%    4.94ms \
16688 requests in 1.00m, 4.85MB read \
Requests/sec:    277.92 \
Transfer/sec:     82.78KB
## 60-10-10
Running 1m test @ http://localhost:8081/ \
10 threads and 10 connections \
Thread Stats   Avg      Stdev     Max   +/- Stdev \
Latency    45.28ms    6.00ms 103.65ms   86.56% \
Req/Sec    22.07      4.50    50.00     75.67% \
Latency Distribution \
50%   44.71ms \
75%   47.24ms \
90%   50.18ms \
99%   75.32ms \
13247 requests in 1.00m, 3.76MB read \
Requests/sec:    220.50 \
Transfer/sec:     64.08KB
## 60-50-50
Running 1m test @ http://localhost:8081/ \
50 threads and 50 connections \
Thread Stats   Avg      Stdev     Max   +/- Stdev \
Latency    55.84ms   30.37ms 108.33ms   54.29% \
Req/Sec    12.88      7.37    30.00     76.92% \
Latency Distribution \
50%   54.04ms \
75%   92.36ms \
90%   96.66ms \
99%  108.33ms \
35 requests in 1.00m, 10.20KB read \
Requests/sec:      0.58 \
Transfer/sec:     173.85B

# Tests with cache
## 60-1-1
Running 1m test @ http://localhost:8082/ \
1 threads and 1 connections \
Thread Stats   Avg      Stdev     Max   +/- Stdev \
Latency     2.06ms    1.33ms  25.91ms   98.90% \
Req/Sec   506.47     29.52   560.00     80.17% \
Latency Distribution \
50%    1.91ms \
75%    2.05ms \
90%    2.21ms \
99%    3.83ms \
30267 requests in 1.00m, 8.60MB read \
Requests/sec:    504.11 \
Transfer/sec:    146.70KB
## 60-10-10
Running 1m test @ http://localhost:8082/ \
10 threads and 10 connections \
Thread Stats   Avg      Stdev     Max   +/- Stdev \
Latency    17.29ms    3.25ms  50.15ms   92.95% \
Req/Sec    58.10      6.24    90.00     69.18% \
Latency Distribution \
50%   16.80ms \
75%   17.92ms \
90%   19.33ms \
99%   31.83ms \
34864 requests in 1.00m, 9.84MB read \
Requests/sec:    580.44 \
Transfer/sec:    167.72KB \
## 60-50-50
Running 1m test @ http://localhost:8082/ \
50 threads and 50 connections \
Thread Stats   Avg      Stdev     Max   +/- Stdev \
Latency    62.50ms  135.38ms 537.64ms   85.42% \
Req/Sec    38.85     50.76   130.00     75.76% \
Latency Distribution \
50%    8.63ms \
75%   10.23ms \
90%  308.84ms \
99%  504.57ms \
144 requests in 1.00m, 41.88KB read \
Requests/sec:      2.40 \
Transfer/sec:     713.62B