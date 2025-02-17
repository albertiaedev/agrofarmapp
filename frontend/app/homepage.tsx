import { useEffect, useState } from "react";
import { getDataFromAves, getDataFromBovinos, getDataFromCerdos, getDataFromEquinos } from "./api";
import Image from "next/image";

export default function Home() {
  const [avesData, setAvesData] = useState(null);
  const [bovinosData, setBovinosData] = useState(null);
  const [cerdosData, setCerdosData] = useState(null);
  const [equinosData, setEquinosData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const aves = await getDataFromAves();
        const bovinos = await getDataFromBovinos();
        const cerdos = await getDataFromCerdos();
        const equinos = await getDataFromEquinos();
        setAvesData(aves);
        setBovinosData(bovinos);
        setCerdosData(cerdos);
        setEquinosData(equinos);
      } catch (error) {
        console.error("Error en el módulo:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <div>
          <h2>Módulo de Producción de Aves:</h2>
          <pre>{JSON.stringify(avesData, null, 2)}</pre>
        </div>
        <div>
          <h2>Módulo de Producción de Bovinos:</h2>
          <pre>{JSON.stringify(bovinosData, null, 2)}</pre>
        </div>
        <div>
          <h2>Módulo de Producción de Cerdos:</h2>
          <pre>{JSON.stringify(cerdosData, null, 2)}</pre>
        </div>
        <div>
          <h2>Módulo de Producción de Equinos:</h2>
          <pre>{JSON.stringify(equinosData, null, 2)}</pre>
        </div>
      </main>
    </div>
  );
}