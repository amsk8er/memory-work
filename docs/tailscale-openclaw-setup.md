# Tailscale + OpenClaw 配置指南

> 适用场景：在 Mac mini 上运行 OpenClaw Gateway，通过 Tailscale 在 tailnet 内安全访问。

---

## 概览

```
MacBook Pro ──── tailnet ──── Mac mini (OpenClaw Gateway :18789)
                                    │
                            Tailscale serve (HTTPS)
                       https://zhangxiaoyoudemac-mini-1.tail7ea35a.ts.net
```

---

## Mac mini 配置

### 1. 安装 Tailscale

```bash
brew install tailscale
```

### 2. 启动 Tailscale 系统服务（需要 root）

```bash
sudo brew services start tailscale
```

> 这一步必须用 `sudo`，tailscaled 需要 root 权限绑定 `/var/run/tailscaled.socket`。
> 成功后开机自动启动，无需重复操作。

### 3. 登录 Tailscale

```bash
tailscale up --qr
```

在浏览器打开输出的 URL（或扫描二维码），用 Tailscale 账号完成授权。

### 4. 配置 OpenClaw

编辑 `~/.openclaw/openclaw.json`，将 `gateway.tailscale.mode` 改为 `serve`：

```json
"gateway": {
  "port": 18789,
  "mode": "local",
  "bind": "loopback",
  "tailscale": {
    "mode": "serve",
    "resetOnExit": false
  }
}
```

### 5. 重启 OpenClaw Gateway

```bash
pkill -f "openclaw-gateway"
```

OpenClaw 会自动重启并执行 `tailscale serve --bg --yes 18789`。

### 6. 验证

```bash
# 检查 Tailscale 节点状态
tailscale status

# 检查 serve 是否生效
tailscale serve status
```

预期输出：

```
https://zhangxiaoyoudemac-mini-1.tail7ea35a.ts.net (tailnet only)
|-- / proxy http://127.0.0.1:18789
```

### 7. 开启 Tailscale Serve 权限（管理后台）

首次配置需要在 Tailscale 后台开启 Serve 功能：

```
https://login.tailscale.com/f/serve?node=nv4p1gbxJq11CNTRL
```

---

## MacBook Pro 配置

MacBook Pro 只需加入同一 tailnet，无需额外配置 OpenClaw。

### 前提

MacBook Pro 已安装 Tailscale 并登录同一账号（tailnet 内可见即可）。

### 访问 OpenClaw

直接在浏览器打开：

```
https://zhangxiaoyoudemac-mini-1.tail7ea35a.ts.net
```

---

## 节点信息

| 设备 | Tailscale IP | 节点名 |
|------|-------------|--------|
| Mac mini | 100.99.104.1 | zhangxiaoyoudemac-mini-1 |
| MacBook Pro | 100.70.122.71 | macbook-pro |

---

## 故障排查

**OpenClaw 启动时报 `dial unix /var/run/tailscaled.socket: no such file or directory`**

tailscaled 未以 root 运行，执行：
```bash
sudo brew services restart tailscale
```

**`tailscale serve status` 显示 `No serve config`**

手动执行一次：
```bash
tailscale serve --bg --yes 18789
```

**Tailscale 节点离线**

```bash
tailscale status       # 查看连接状态
sudo brew services restart tailscale  # 重启服务
```
