### Stock Market lookup plugin for Sarah 

Make Sarah check the stock market for you using [marketwatch.com](http://www.marketwatch.com/)

usage : 
```bash
$ sarah marketwatch lookup_term [country] [security_type]
```
example : 
```bash
$ sarah marketwatch googl us stock
$ sarah marketwatch yamaha jp
$ sarah marketwatch AMD
```

#### country options
`country_option` | actual country name
* `us` | United States of America (default)
* `all` | All countries
* `ca` | Canada
* `au` | Australia
* `fr` | France
* `de` | Germany
* `hk` | Hong Kong
* `it` | Italy
* `jp` | Japan
* `nl` | Netherlands 
* `nz` | New Zealand
* `no` | Norway
* `za` | South Africa
* `es` | Spain
* `se` | Sweden
* `ch` | Switzerland
* `uk` | United Kingdom
#### security_type options
* `All` (default)
* `Stock`
* `Fund`
* `Index` 
* `Currency`
