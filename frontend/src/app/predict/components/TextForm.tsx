"use client";

import { TextField, Button } from "@mui/material";

type Props = {
  text: string;
  onTextChange: (value: string) => void;
  onSubmit: () => void;
};

export default function TextForm({ text, onTextChange, onSubmit }: Props) {
  return (
    <>
      <TextField
        fullWidth
        label="文章を入力してください"
        multiline
        rows={4}
        value={text}
        onChange={(e) => onTextChange(e.target.value)}
        sx={{ mb: 2 }}
      />
      <Button variant="contained" color="primary" fullWidth onClick={onSubmit}>
        予測する
      </Button>
    </>
  );
}
