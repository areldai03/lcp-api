"use client";

import { useState } from "react";
import { Container, Typography, TextField, Button, Card, CardContent, FormControl, MenuItem, InputLabel, Select, StyledEngineProvider, SelectChangeEvent } from "@mui/material";

export default function PredictPage() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<null | { difficulty: number; method: string }>(null);
  const [method, setMethod] = useState<"wordfreq" | "rule" | "embedding">("wordfreq");

  const handleSubmit = async () => {
    try {
      const response = await fetch(`http://localhost:8000/predict?method=${method}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error("Prediction failed");
      }

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

      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel id="method-select-label">予測手法</InputLabel>
        <Select
          labelId="method-select-label"
          id="method-select"
          value={method}
          label="予測手法"
          onChange={handleMethodChange}
        >
          <MenuItem value="wordfreq">単語頻度</MenuItem>
          <MenuItem value="rule">ルールベース</MenuItem>
          <MenuItem value="embedding">埋め込み</MenuItem>
        </Select>
      </FormControl>

      <TextField
        fullWidth
        label="文章を入力してください"
        multiline
        rows={4}
        value={text}
        onChange={(e) => setText(e.target.value)}
        sx={{ mb: 2 }}
      />

      <Button variant="contained" color="primary" fullWidth onClick={handleSubmit}>
        予測する
      </Button>

      {result && (
        <Card sx={{ mt: 4 }}>
          <CardContent>
            <Typography variant="h6">予測結果</Typography>
            <Typography>難易度: {result.difficulty}</Typography>
            <Typography>手法: {result.method}</Typography>
          </CardContent>
        </Card>
      )}
    </Container>
    </StyledEngineProvider>
  );
}
