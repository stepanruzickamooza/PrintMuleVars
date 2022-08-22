# PrintMuleVars

Python script which will help you to flatten Yaml configuration file, print variables from configuration file in XML format (pom.xml) or as command line arguments, e.g. -Dvariable_name=${variable_name}

### Flatten Yaml Variables
```python
python print_mule_vars.py -f src/boe-sys-insphire/src/main/resources/boe-sys-insphire-config.yaml
```
...
insphire.replica.db.host=192.168.18.32
insphire.replica.db.port=1433
insphire.replica.db.databasename=IHDATA
insphire.replica.db.user=MuleSoftUserDev
boe-sys-outsystems.host=tst.integratewith.boels.com
boe-sys-outsystems.port=443
boe-sys-outsystems.path=/sys/outsystems/api/crossreferences
boe-sys-outsystems.timeout=20000
boe-sys-outsystems.username=boels-integration

### Flatten Yaml Variables for One System Only
```python
python print_mule_vars.py -f src/boe-sys-insphire/src/main/resources/boe-sys-insphire-config.yaml -i boe-sys-outsystems
```

boe-sys-outsystems.host=tst.integratewith.boels.com
boe-sys-outsystems.port=443
boe-sys-outsystems.path=/sys/outsystems/api/crossreferences
boe-sys-outsystems.timeout=20000
boe-sys-outsystems.username=boels-integration

### Print Yaml Variables as Mule Arguments
```python
python print_mule_vars.py -f src/boe-sys-insphire/src/main/resources/boe-sys-insphire-config.yaml -i boe-sys-outsystems -r='-D\1=$(tst-\1)'
```

-Dboe-sys-outsystems.host=$(tst-boe-sys-outsystems.host)
-Dboe-sys-outsystems.port=$(tst-boe-sys-outsystems.port)
-Dboe-sys-outsystems.path=$(tst-boe-sys-outsystems.path)
-Dboe-sys-outsystems.timeout=$(tst-boe-sys-outsystems.timeout)
-Dboe-sys-outsystems.username=$(tst-boe-sys-outsystems.username)
-Dboe-sys-outsystems.password=$(tst-boe-sys-outsystems.password)

### Print Yaml Variables as XML variables
```python
python /Users/stepanruzicka/Workspace/scripts/bin/print_mule_vars/print_mule_vars.py -f src/boe-sys-insphire/src/main/resources/boe-sys-insphire-config.yaml -i boe-sys-outsystems -r='<\1>${\1}<\\\1>'
```
* *
<boe-sys-outsystems.host>${boe-sys-outsystems.host}<\boe-sys-outsystems.host>
<boe-sys-outsystems.port>${boe-sys-outsystems.port}<\boe-sys-outsystems.port>
<boe-sys-outsystems.path>${boe-sys-outsystems.path}<\boe-sys-outsystems.path>
<boe-sys-outsystems.timeout>${boe-sys-outsystems.timeout}<\boe-sys-outsystems.timeout>
<boe-sys-outsystems.username>${boe-sys-outsystems.username}<\boe-sys-outsystems.username>
<boe-sys-outsystems.password>${boe-sys-outsystems.password}<\boe-sys-outsystems.password>
* *

### Print Yaml Variables as Mule Arguments with Original Values as Values
```python
python /Users/stepanruzicka/Workspace/scripts/bin/print_mule_vars/print_mule_vars.py -f src/boe-sys-insphire/src/main/resources/boe-sys-insphire-config.yaml -i boe-sys-outsystems  -r='-D\1=\2' -s " "
```

-Dboe-sys-outsystems.host=tst.integratewith.boels.com -Dboe-sys-outsystems.port=443 -Dboe-sys-outsystems.path=/sys/outsystems/api/crossreferences -Dboe-sys-outsystems.timeout=20000 -Dboe-sys-outsystems.username=boels-integration
