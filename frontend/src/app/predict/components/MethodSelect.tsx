"use client";

import { FormControl, InputLabel, MenuItem, Select, SelectChangeEvent } from "@mui/material";

type Method = "wordfreq" | "rule" | "embedding";

type Props = {
  method: Method;
  onChange: (event: SelectChangeEvent<Method>) => void;
};

export default function MethodSelect({ method, onChange }: Props) {
  return (
    <FormControl fullWidth sx={{ mb: 2 }}>
      <InputLabel id="method-select-label">予測手法</InputLabel>
      <Select
        labelId="method-select-label"
        value={method}
        label="予測手法"
        onChange={onChange}
      >
        <MenuItem value="wordfreq">単語頻度</MenuItem>
        <MenuItem value="rule">ルールベース</MenuItem>
        <MenuItem value="embedding">埋め込み</MenuItem>
      </Select>
    </FormControl>
  );
}
