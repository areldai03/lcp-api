"use client";

import { Card, CardContent, Typography } from "@mui/material";

type Props = {
  result: {
    difficulty: number;
    method: string;
  };
};

export default function ResultCard({ result }: Props) {
  return (
    <Card sx={{ mt: 4 }}>
      <CardContent>
        <Typography variant="h6">予測結果</Typography>
        <Typography>難易度: {result.difficulty}</Typography>
        <Typography>手法: {result.method}</Typography>
      </CardContent>
    </Card>
  );
}
