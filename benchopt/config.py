import os
import re
import configparser


CONFIG_FILE_LOCATION = os.environ.get('BENCHO_CONFIG', './benchopt.ini')

config = configparser.ConfigParser()
config.read(CONFIG_FILE_LOCATION)


DEFAULT_GLOBAL = {
    'debug': False,
    'allow_install': False,
    'print_install_error': False,
    'venv_dir': './.venv/',
    'cache_dir': '.',
}

DEFAULT_BENCHMARK = {
    'exclude_solvers': "[]",
}


def get_global_setting(name):
    assert name in DEFAULT_GLOBAL, f"Unkonwn config key {name}"

    # TODO: get the correct type from DEFAULT_GLOBAL

    if isinstance(DEFAULT_GLOBAL[name], bool):
        setting = config.getboolean('benchopt', name,
                                    fallback=DEFAULT_GLOBAL[name])
    else:
        setting = config.get('benchopt', name, fallback=DEFAULT_GLOBAL[name])
    return setting


def get_benchmark_setting(benchmark, name):
    setting = config.get(benchmark, name, fallback=DEFAULT_BENCHMARK[name])
    if name == 'exclude_solvers':
        setting = re.findall("[\"']([^']+)[\"']", setting)
    return setting
