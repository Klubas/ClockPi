# ClockPi

## Todo
* Criar uma API para permitir configuração remota
* ~Permitir configurar vários alarmes (todos usando o mesmo scheduler)~
* Salvar configurações e alarmes configurados em json
* Criar uma interface web para configuração
* Permitir maior variedade de períodos e repetição de alarmes
* Cancelar alarmes por identificador
* Cancelar alarmes por tag

## Usage

* Starting the server

		clockpy.py --hostname <hostname>:<port> [--debug]
		clockpi.py --hostname localhost:8080


* Scheduling alarms via API

		curl -X POST -H "Content-Type: application/json" -d '{"hour":"07:00"}' http://localhost:8080/new_alarm
 ## Links
 
 * Pinout
 
 	https://pinout.xyz/pinout/pin16_gpio23#
 
 * LCD
 
 	https://pimylifeup.com/raspberry-pi-lcd-16x2/
