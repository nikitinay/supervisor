import argparse 
import daemon

ARG_PARSER = argparse.ArgumentParser()
ARG_PARSER.add_argument(
    '--restart_interval',
    default=1,
    help="seconds between to restart",
    required=False)
ARG_PARSER.add_argument(
    '--max_restarts',
    default=3,
    help="number of restarts",
    required=False)
ARG_PARSER.add_argument(
    '--process_name',
    default="PROCESS",
    help="name of the process",
    required=False)
ARG_PARSER.add_argument(
    '--check_interval',
    default=5,
    help="check interval in seconds",
    required=False)
ARG_PARSER.add_argument(
    '--command',
    help="command to start the process",
    required=False)

ARGUMENTS = ARG_PARSER.parse_args()

restart_interval = ARGUMENTS.restart_interval
max_restarts = ARGUMENTS.max_restarts
process_name = ARGUMENTS.process_name
check_interval = ARGUMENTS.check_interval
command = ARGUMENTS.command

if command is None:
    command = input("command to start the process: ")    

if int(restart_interval) < 0:
    print("restart_interval must be greater or equal than 0")
    daemon.logger.error("restart_interval must be greater or equal than 0")
    exit()

if int(max_restarts) < 0:
    print("max_restarts must be greater or equal than 0")
    daemon.logger.error("max_restarts must be greater or equal than 0")
    exit()

if int(check_interval) < 0:
    print("check_interval must be greater or equal than 0")
    daemon.logger.error("check_interval must be greater or equal than 0")
    exit()