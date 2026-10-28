# Unbeatable Tic-Tac-Toe
- `tictactoe/engine.py` - minimax + alpha-beta pruning, greedy move ordering (centre > corners > edges)
- `cli.py` - play in terminal: `python cli.py`
- `api/move.py` - Vercel Python serverless endpoint `POST /api/move`
- `index.html` - UI: pick X, O or Random. Falls back to an identical JS engine if the API is unreachable.

## Deploy
```
npm i -g vercel
vercel --prod
```
(or push to GitHub and import the repo at vercel.com/new - no build settings needed)
