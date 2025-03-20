### ExpNext

ExpNext Accounting

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/erpnext-thailand/expnext.git --branch develop
bench --site [site-name] install-app expnext
bench --site [site-name] migrate
bench --site [site-name] clear-cache
bench start
```

### Contributing

```bash
docker-compose up -d
docker-compose exec -it frappe bash
cd frappe-bench
# type your bench command
bench start
```
### License

mit
