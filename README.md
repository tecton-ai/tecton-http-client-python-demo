# Demo Application for Tecton Python Client Library

This is a demo client to use the Tecton Python Client library to retrieve features and metadata information from the
Tecton Online Feature Store.

## Documentation


* [Fetching Online Features](https://docs.tecton.ai/latest/examples/fetch-real-time-features.html)

* [FeatureServer API Reference](https://docs.tecton.ai/rest-swagger/docs.html)

* [Tecton Python Client API Reference](https://tecton-ai.github.io/tecton-http-client-python/html/index.html)


## Benchmarking Results

For get-features/ requests, the following benchmark statistics were observed.

| Percentile | Value         |
|------------|---------------|
| P50        | 0.0995730162  |
| P90        | 0.1031625271  |
| P95        | 0.1068629026  |
| P99        | 0.1257531643  |


For get-features-batch/ requests, with 10 requests, the following benchmark statistics were observed.

| Micro Batch Size | P50           | P90           | P95          | P99           |
|------------------|---------------|---------------|--------------|---------------|
| 1                | 0.0940459967  | 0.107743001   | 0.1160096884 | 0.1347592211  |
| 2                | 0.0909669399  | 0.1059193611  | 0.1144580126 | 0.129556427   |
| 3                | 0.0948300362  | 0.1060825109  | 0.113814044  | 0.1297174358  |
| 4                | 0.0926214457  | 0.1033223867  | 0.1116884947 | 0.1241452694  |
| 5                | 0.1111600399  | 0.1213054656  | 0.1283767223 | 0.1426982283  |

With 50 requests, the following benchmark statistics were observed.

| Micro Batch Size | P50           | P90           | P95           | P99           |
|------------------|---------------|---------------|---------------|---------------|
| 1                | 0.5354094505  | 0.5661278248  | 0.5931284428  | 0.8217940950  |
| 2                | 0.3278810978  | 0.3438197613  | 0.3538464665  | 0.4103030014  |
| 3                | 0.2323441505  | 0.2470543385  | 0.2563468218  | 0.3363552046  |
| 4                | 0.1409490108  | 0.1521555424  | 0.1571177006  | 0.1981020546  |

With 100 requests, the following benchmark statistics were observed.

| Micro Batch Size | P50           | P90           | P95           | P99           |
|------------------|---------------|---------------|---------------|---------------|
| 1                | 0.9110641479  | 0.9508376122  | 0.9694476128  | 1.0972022867  |
| 2                | 0.4828045368  | 0.5101396084  | 0.5266952634  | 0.5759255052  |
| 3                | 0.3709440231  | 0.391367197   | 0.4032581806  | 0.5664810371  |




## Troubleshooting


If you have any questions or need help, please [open an Issue](https://github.com/tecton-ai/tecton-http-client-python)
or reach out to us on Slack!


## License

The project is licensed
under [Apache License 2.0](https://github.com/tecton-ai/tecton-http-client-java/blob/main/LICENSE.md)
