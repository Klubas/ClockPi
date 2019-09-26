# ClockPi

## Todo
* Criar uma API para permitir configuração remota
* ~Permitir configurar vários alarmes (todos usando o mesmo scheduler)~
* Salvar configurações e alarmes configurados em json
* Criar uma interface web para configuração 

## Usage

* Starting the server

		clockpy.py --hostname <hostname>:<port> [--debug]
		clockpi.py localhost:8080 True


* Scheduling alarms via API

		curl -X POST -H "Content-Type: application/json" -d '{"hour":"07:00"}' http://localhost:8080/new_alarm
