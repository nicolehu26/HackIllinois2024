# HackIllinois 2024 Hardware Track - Autonomous Vehicle

## Team
Celina Anwar, Madhumita Narayan, Nicole Hu, Shreya Perumalla

UIUC Computer Science

<p align="center">
  <strong>Autonomous Vehicles</strong>
</p>

John Deere innovates on behalf of humanity.

It doesn’t matter if you’ve never driven a tractor, mowed a lawn, or operated a dozer. With our role in helping produce food, fiber, fuel, and infrastructure, we work for every single person on the planet.

<div style="display: flex; justify-content: center">
  <div style="display: flex; flex-direction: column; width: 75%">
    <p align="center">
      <em>
        "We don’t create tech for tech’s sake. There’s purpose behind everything we do, so that our customers have the tools they need to tackle some of the world’s greatest challenges."
      </em>
      <br><br>
      <strong>John May</strong>
      <br>
      <em>Chairman and CEO | John Deere</em>
  </div>
</div>

Now, let's see what you can build.

<br>
<br>

<p align="center">
  <strong>Build your own autonomous vehicle</strong>
</p>

<br>

For your HackIllinois 2024 John Deere prompt, <strong>you are tasked with building your own autonomous vehicle, a vehicle that solves any problem that you define.</strong>

It is up to each team to determine what _problem_ your vehicle solves. Does it drive down the road? Deliver food? Solve a maze? Plant a corn field? It could be something useful, something fun, or anything you can imagine. The only stipulation is that your vehicle:

- Solves the problem autonomously, that is, makes decisions on its own
- Uses data from sensor(s) in its decisions

Each team is supplied with a [hardware kit](#john-deere-kit). Teams are welcome to add to the vehicle and kit as needed. Teams are not required to use all items in the kit.

Like many problems at John Deere, this prompt requires more than just a software solution, it requires a solution at the intersection of mechanical systems, electrical systems, sensors, data, automation, programming, and of course, creativity.

Good luck!

## Our Submission

## What it does / Development
Using the OpenCV computer vision library and live input from a raspberry pi camera feed, our bot detects areas of a field in need of fertilizing. The bot stops on these areas, represented by the color blue, then moves on. Thus, the bot will not fertilize any areas other than what’s necessary. 

## How we built it
- **Vehicle Chassis**
  - 2 Rubber wheels
  - 2 Speed encoders
  - Swivel wheel and connectors
  - Acrylic frame
  - 3D Printed battery frame
- **Raspberry Pi**
  - Raspberry Pi 4 Model B 4GB RAM
  - 64 GB Micro SDXC Card
  - Ethernet Cable
  - USB-C to Ethernet Adapter
- **Power**
  - 10,000mAh Rechargeable Battery
  - USB-C to USB-C: for powering Raspberry Pi / recharing battery
  - USB-A to Micro USB: for powering Raspberry Pi HAT / motors
- **Electronics**
  - Printed Circuit Board
  - 2 Button Switches - to be read by Raspberry Pi
  - Slide Switch - to control motor power circuit
  - 2 LEDs
  - H-Bridge
  - Camera
  - 2 Ultrasonic Distance Sensors
  - 2 Electric Motors

## Challenges We Ran Into
Managed to short-circuit our sensor with only 5 volts
Configuring our new functions with the “brain”

## Accomplishments / What We Learned
OpenCV computer vision library
Live input from a raspberry pi camera feed

## What's Next for HarvestHer
Add live video feed
Detect various shades of green or soil conditions
More sensitive object detection
