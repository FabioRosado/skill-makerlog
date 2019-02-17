# opsdroid skill Makerlog

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to send tasks to Makerlog.

## Requirements

Makerlog webhook url obtained from [Makerlog webhook app](https://getmakerlog.com/apps/webhooks).

## Configuration

```yaml
  - name: makerlog
    webhook: https://api.getmakerlog.com/apps/webhook/Litxo2930UI
```

## Usage

_Note: Opsdroid will reply the same way to both `add task -` and `completed task -` commands. Head over to [makerlog](https://getmakerlog.com/) to see the tasks that were added._

#### `add task - <my task>`

Adds to do task to makerlog - this will be an unfinished task.

> user: add task - Refactor code
>
> opsdroid: Added to do task 'Refactor code' to makerlog

#### `completed task - <my task>`

Adds to do task to makerlog - this will be an unfinished task.

> user: add task - Refactor code
>
> opsdroid: Added to do task 'Refactor code' to makerlog
