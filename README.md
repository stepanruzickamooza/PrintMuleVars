# PrintMuleVars

Python script which will help you to flatten Yaml configuration file, print variables from configuration file in XML format (pom.xml) or as command line arguments, e.g. -Dvariable_name=${variable_name}

```bash
usage: print_mule_vars.py [-h] [-d] -f FILE [-i ITEM] [-r REGULAREXPRESSION] [-s SEPARATOR]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Debug mode
  -f FILE, --file FILE  Input yaml file
  -i ITEM, --item ITEM  Item
  -r REGULAREXPRESSION, --replace-regular-expression REGULAREXPRESSION
                        Regular expression
  -s SEPARATOR, --output-separator SEPARATOR
                        Output separator
```

In your regular expressions you can use
* \1 - Represents the key
* \2 - Represents the value

## EXAMPLES
Let's say we have the following config file...

```
wire:
  db:
    host: "192.168.18.32"
    port: "1433" 
    databasename: "IHDATA"   
    user: "MuleSoftUserDev"
zoe-sys-example:
  host: "tst.integratewith.zoels.com"
  port: "443"
  path: "/sys/example/api/crossreferences"
  timeout: "20000"
  username: "zoels-integration"
```

### Flatten Yaml Variables
```python
python print_mule_vars.py -f src/zoe-sys-wire/src/main/resources/zoe-sys-wire-config.yaml
```
```
...
wire.replica.db.host=192.168.18.32
wire.replica.db.port=1433
wire.replica.db.databasename=IHDATA
wire.replica.db.user=MuleSoftUserDev
zoe-sys-example.host=tst.integratewith.zoels.com
zoe-sys-example.port=443
zoe-sys-example.path=/sys/example/api/crossreferences
zoe-sys-example.timeout=20000
zoe-sys-example.username=zoels-integration
```

### Flatten Yaml Variables for One System Only
```python
python print_mule_vars.py -f src/zoe-sys-wire/src/main/resources/zoe-sys-wire-config.yaml -i zoe-sys-example
```

```
zoe-sys-example.host=tst.integratewith.zoels.com
zoe-sys-example.port=443
zoe-sys-example.path=/sys/example/api/crossreferences
zoe-sys-example.timeout=20000
zoe-sys-example.username=zoels-integration
```

### Print Yaml Variables as Mule Arguments
```python
python print_mule_vars.py -f src/zoe-sys-wire/src/main/resources/zoe-sys-wire-config.yaml -i zoe-sys-example -r='-D\1=$(tst-\1)'
```

```
-Dzoe-sys-example.host=$(tst-zoe-sys-example.host)
-Dzoe-sys-example.port=$(tst-zoe-sys-example.port)
-Dzoe-sys-example.path=$(tst-zoe-sys-example.path)
-Dzoe-sys-example.timeout=$(tst-zoe-sys-example.timeout)
-Dzoe-sys-example.username=$(tst-zoe-sys-example.username)
-Dzoe-sys-example.password=$(tst-zoe-sys-example.password)
```

### Print Yaml Variables as XML variables
```python
python /Users/stepanruzicka/Workspace/scripts/bin/print_mule_vars/print_mule_vars.py -f src/zoe-sys-wire/src/main/resources/zoe-sys-wire-config.yaml -i zoe-sys-example -r='<\1>${\1}<\\\1>'
```
```
<zoe-sys-example.host>${zoe-sys-example.host}<\zoe-sys-example.host>
<zoe-sys-example.port>${zoe-sys-example.port}<\zoe-sys-example.port>
<zoe-sys-example.path>${zoe-sys-example.path}<\zoe-sys-example.path>
<zoe-sys-example.timeout>${zoe-sys-example.timeout}<\zoe-sys-example.timeout>
<zoe-sys-example.username>${zoe-sys-example.username}<\zoe-sys-example.username>
<zoe-sys-example.password>${zoe-sys-example.password}<\zoe-sys-example.password>
```

### Print Yaml Variables as Mule Arguments with Original Values as Values
```python
python /Users/stepanruzicka/Workspace/scripts/bin/print_mule_vars/print_mule_vars.py -f src/zoe-sys-wire/src/main/resources/zoe-sys-wire-config.yaml -i zoe-sys-example  -r='-D\1=\2' -s " "
```

```
-Dzoe-sys-example.host=tst.integratewith.zoels.com -Dzoe-sys-example.port=443 -Dzoe-sys-example.path=/sys/example/api/crossreferences -Dzoe-sys-example.timeout=20000 -Dzoe-sys-example.username=zoels-integration
```
