# supervisor


<details><summary>docker run -it  nikitinay/supervisor --restart_interval 1 --max_restarts 5 --process_name "bash" --check_interval 5 --command 'bash -c "sleep 1 && exit 0"'</summary>
<p>

```
2021-03-28 14:33:03,248:INFO:######## arguments ########
        restart_interval = 1,
        max_restarts = 5 ,
        process_name = bash ,
        check_interval = 5 ,
        command = bash -c "sleep 1 && exit 0"

2021-03-28 14:33:04,250:INFO:starting bash
2021-03-28 14:33:07,259:INFO:starting bash
2021-03-28 14:33:10,266:INFO:starting bash
2021-03-28 14:33:13,274:INFO:starting bash
2021-03-28 14:33:16,281:INFO:starting bash
2021-03-28 14:33:17,286:ERROR:max number of restarts reached
```
</p>
</details>

<details><summary>docker run -it  nikitinay/supervisor --restart_interval 1 --max_restarts 5 --process_name "bash" --check_interval 5 --command 'bash -c "sleep 5 && exit 0"'</summary>
<p>

```
2021-03-28 14:33:50,994:INFO:######## arguments ########
        restart_interval = 1,
        max_restarts = 5 ,
        process_name = bash ,
        check_interval = 5 ,
        command = bash -c "sleep 5 && exit 0"

2021-03-28 14:33:51,996:INFO:starting bash
2021-03-28 14:33:59,004:INFO:starting bash
2021-03-28 14:34:06,011:INFO:starting bash
2021-03-28 14:34:13,020:INFO:starting bash
2021-03-28 14:34:20,037:INFO:starting bash
2021-03-28 14:34:25,052:ERROR:max number of restarts reached
```

</p>
</details>

<details><summary>docker run -it  nikitinay/supervisor --restart_interval 1 --max_restarts 5 --process_name "bash" --check_interval 5 --command 'bash -c "sleep 1 && exit 1"'</summary>
<p>

```
2021-03-28 14:34:56,447:INFO:######## arguments ########
        restart_interval = 1,
        max_restarts = 5 ,
        process_name = bash ,
        check_interval = 5 ,
        command = bash -c "sleep 1 && exit 1"

2021-03-28 14:34:57,449:INFO:starting bash
2021-03-28 14:35:00,457:INFO:starting bash
2021-03-28 14:35:03,464:INFO:starting bash
2021-03-28 14:35:06,476:INFO:starting bash
2021-03-28 14:35:09,485:INFO:starting bash
2021-03-28 14:35:10,490:ERROR:max number of restarts reached
```

</p>
</details>

<details><summary>docker run -it  nikitinay/supervisor --restart_interval 1 --max_restarts 5 --process_name "bash" --check_interval 5 --command 'sh -c "sleep 10 && exit 1"'</summary>
<p>

```
2021-03-28 14:35:26,588:INFO:######## arguments ########
        restart_interval = 1,
        max_restarts = 5 ,
        process_name = bash ,
        check_interval = 5 ,
        command = sh -c "sleep 10 && exit 1"

2021-03-28 14:35:27,590:INFO:starting bash
2021-03-28 14:35:39,596:INFO:starting bash
2021-03-28 14:35:51,602:INFO:starting bash
2021-03-28 14:36:03,607:INFO:starting bash
2021-03-28 14:36:15,614:INFO:starting bash
2021-03-28 14:36:25,616:ERROR:max number of restarts reached
```

</p>
</details>

<details><summary>docker run -it  nikitinay/supervisor --restart_interval 1 --max_restarts 5 --process_name "bash" --check_interval 5 --command 'bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"'</summary>
<p>

```
2021-03-28 14:36:53,148:INFO:######## arguments ########
        restart_interval = 1,
        max_restarts = 5 ,
        process_name = bash ,
        check_interval = 5 ,
        command = bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"

2021-03-28 14:36:54,150:INFO:starting bash
2021-03-28 14:37:06,163:INFO:starting bash
2021-03-28 14:37:08,170:INFO:starting bash
2021-03-28 14:37:10,176:INFO:starting bash
2021-03-28 14:37:12,183:INFO:starting bash
2021-03-28 14:37:12,194:ERROR:max number of restarts reached
```

</p>
</details>

<details><summary>docker run -it  nikitinay/supervisor --restart_interval 1 --max_restarts 1 --process_name "bash" --check_interval 5 --command 'bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"'</summary>
<p>

```
2021-03-28 14:37:35,096:INFO:######## arguments ########
        restart_interval = 1,
        max_restarts = 1 ,
        process_name = bash ,
        check_interval = 5 ,
        command = bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"

2021-03-28 14:37:36,099:INFO:starting bash
2021-03-28 14:37:46,108:ERROR:max number of restarts reached
```
</p>
</details>
