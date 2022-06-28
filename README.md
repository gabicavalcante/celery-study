Open worker shell:

```shell
$ docker exec -it celery-workflow-chords_worker_1 /bin/bash
```

Run script:

```shell
➜  celery-workflow-chords docker exec -it celery-workflow-chords_worker_1 /bin/bash
root@70254f9c94fe:/app# ipython
Python 3.9.12 (main, Mar 25 2022, 00:17:14) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from group_test import run

In [2]: run()
```