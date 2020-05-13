Docker for mac 安装 Istio https://www.jianshu.com/p/131bf15235b1?from=timeline&isappinstalled=0
[Istio] 外部访问Istio自带的Prometheus和Grafana https://blog.csdn.net/blanchedingding/article/details/84109400
istio 从入门到放弃系列 https://blog.51cto.com/14268033/2479177
远程访问遥测插件 https://preliminary.istio.io/zh/docs/tasks/observability/gateways/
Kiali——Istio Service Mesh 的可观察性工具 https://www.yunforum.net/group-topic-id-2217.html
istio 可视化工具 kiali 部署体验 https://www.zhihu.com/tardis/sogou/art/41324294
Bookinfo 应用 https://preliminary.istio.io/zh/docs/examples/bookinfo/

apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: kiali-gateway
  namespace: istio-system
spec:
  selector:
    istio: ingressgateway # use Istio default gateway implementation
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "kiali.lswzw.com"
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: kiali-gateway
  namespace: istio-system 
spec:
  gateways:
  - kiali-gateway
  hosts:
  - kiali.lswzw.com
  http:
  - route:
    - destination:
        host: kiali
        port:
          number: 20001

istioctl manifest apply --set profile=demo    \
 --set values.global.jwtPolicy=third-party-jwt      \
--set values.gateways.istio-ingressgateway.telemetry_addon_gateways.prometheus_gateway.enabled=true \
--set addonComponents.grafana.enabled=true \
--set values.gateways.istio-ingressgateway.telemetry_addon_gateways.grafana_gateway.enabled=true \
--set addonComponents.kiali.enabled=true \
--set values.kiali.createDemoSecret=true \
--set values.gateways.istio-ingressgateway.telemetry_addon_gateways.kiali_gateway.enabled=true \
--set addonComponents.tracing.enabled=true \
--set values.gateways.istio-ingressgateway.telemetry_addon_gateways.tracing_gateway.enabled=true


quay.io/kiali/kiali:v1.15