# io-process-docker-benchmark
Running `bash run_docker.sh $PWD/test/` on a local computer give me:
```
Time to generate and save images: 24.84 seconds
Time to load and convert images: 5.87 seconds
```
Running it on simon1 as `bash run_docker.sh /mnt/ai4ar/test/` prints:
```
Time to generate and save images: 47.80 seconds
Time to load and convert images: 8.64 seconds
```
And running it on simon2 I'll have:
```
Time to generate and save images: 134.38 seconds                                                                                                                         
Time to load and convert images: 12.38 seconds
```
