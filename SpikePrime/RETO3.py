import motor
from hub import port
import force_sensor, runloop, time

async def main():
    estado_anterior = False

    while True:
        fuerza = force_sensor.force(port.E)
        presionado = fuerza > 9

        if presionado != estado_anterior:
            if presionado:
                motor.run_for_degrees(port.A, -90, 100)
            else:
                motor.run_for_degrees(port.A, 90, 100)

            estado_anterior=presionado

        await runloop.sleep_ms(100)

runloop.run(main())