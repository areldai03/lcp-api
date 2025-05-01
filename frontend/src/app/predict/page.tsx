"use client";

import { useState } from "react";
import { Container, Typography, StyledEngineProvider } from "@mui/material";
import TextForm from "./components/TextForm";
import MethodSelect from "./components/MethodSelect";
import ResultCard from "./components/ResultCard";
import { SelectChangeEvent } from "@mui/material/Select";

export default function PredictPage() {
  const [text, setText] = useState("");
  const [method, setMethod] = useState<"wordfreq" | "rule" | "embedding">("wordfreq");
  const [result, setResult] = useState<null | { difficulty: number; method: string }>(null);

  const handleSubmit = async () => {
    try {
      const response = await fetch(`http://localhost:8000/predict?method=${method}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) throw new Error("Prediction failed");
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      setResult(null);
    }
  };

  const handleMethodChange = (event: SelectChangeEvent<"wordfreq" | "rule" | "embedding">) => {
    setMethod(event.target.value as "wordfreq" | "rule" | "embedding");
  };

  return (
    <StyledEngineProvider injectFirst>
      <Container maxWidth="sm" sx={{ mt: 8 }}>
        <Typography variant="h4" align="center" gutterBottom>
          難易度予測アプリ
        </Typography>
        <MethodSelect method={method} onChange={handleMethodChange} />
        <TextForm text={text} onTextChange={setText} onSubmit={handleSubmit} />
        {result && <ResultCard result={result} />}
      </Container>
    </StyledEngineProvider>
  );
}
