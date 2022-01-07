# Darkly

| Url              | Vulnerabilite           | Flag                                                               |
|------------------|-------------------------|:------------------------------------------------------------------:|
| /.hidden         | Broken Access Control   | `99dde1d35d1fdd283924d84e6d9f1d820`                                |
| Cookie           | Broken Authentification | `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3` |
| /?page=e43ad1... | HTTP Header             | `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188` |
| /?page\=recover  | Insecure Design         | `1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0` |   
| /?page=../       | LFI                     | `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0` |
| /?page=survey    | Fake Vote               | `03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa` |
| /?page=redirect  | Redirect                | `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3` |
| /?page=searchimg | SQL Injection Images    | `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188` |
| /?page=member    | SQL Injection Member    | `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5` |
| /?page=upload    | Upload PHP              | `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8` |
| /?page=signin    | Weak Password           | `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2` |
| /?page=feedback  | XSS Injection           | `0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e` |
| /?page=media     | Object                  | `928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d` |
| /whatever        | Leak Password           | `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff` |
