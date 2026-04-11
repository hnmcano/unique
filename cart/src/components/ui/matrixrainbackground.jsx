// matrixrainbackground.jsx
"use client"

import { Canvas, useFrame } from "@react-three/fiber"
import { useRef, useMemo } from "react"
import * as THREE from "three"

function RainLayer({ speed = 0.05, opacity = 0.5, count = 150 }) {
  const group = useRef(null)

  const lines = useMemo(() => {
    const temp = []

    for (let i = 0; i < count; i++) {
      const x = Math.random() * 20 - 10
      const y = Math.random() * 20 - 10
      const z = Math.random() * -10

      const length = Math.random() * 1.2 + 0.5

      const points = [
        new THREE.Vector3(x, y, z),
        new THREE.Vector3(x - 0.4, y - length, z),
      ]

      const geometry = new THREE.BufferGeometry().setFromPoints(points)

      const material = new THREE.LineBasicMaterial({
        color: Math.random() > 0.5 ? "#ff0000" : "#585757",
        transparent: true,
        opacity,
      })

      const line = new THREE.Line(geometry, material)
      temp.push(line)
    }

    return temp
  }, [count, opacity])

  useFrame(() => {
    lines.forEach((line) => {
      line.position.y -= speed
      line.position.x -= speed * 0.5

      if (line.position.y < -10) {
        line.position.y = 10
        line.position.x = Math.random() * 20 - 10
      }
    })
  })

  return (
    <group ref={group}>
      {lines.map((line, i) => (
        <primitive key={i} object={line} />
      ))}
    </group>
  )
}

// partículas (faíscas)
function Sparks() {
  const pointsRef = useRef(null)

  const particles = useMemo(() => {
    const positions = []

    for (let i = 0; i < 200; i++) {
      positions.push(
        Math.random() * 20 - 10,
        Math.random() * 20 - 10,
        Math.random() * -10
      )
    }

    return new Float32Array(positions)
  }, [])

  useFrame(() => {
    if (pointsRef.current) {
      pointsRef.current.rotation.y += 0.0005
    }
  })

  return (
    <points ref={pointsRef}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={particles.length / 3}
          array={particles}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial size={0.03} color="#ff0000" transparent opacity={0.6} />
    </points>
  )
}

export default function MatrixRainBackground() {
  return (
    <div className="absolute inset-0 z-0">
      <Canvas camera={{ position: [0, 0, 5], fov: 60 }}>
        <fog attach="fog" args={["#000000", 5, 20]} />

        {/* camadas (profundidade) */}
        <RainLayer speed={0.03} opacity={0.2} count={100} />
        <RainLayer speed={0.05} opacity={0.4} count={150} />
        <RainLayer speed={0.08} opacity={0.8} count={200} />

        <Sparks />
      </Canvas>
    </div>
  )
}