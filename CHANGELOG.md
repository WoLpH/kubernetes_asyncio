# v11.3.0

* fix: watch closes http session ([#104](https://github.com/tomplus), [@tomplus](https://github.com/tomplus))

# v11.2.0

* feat: regenerate client against openapi-generator v4.3.0 (context-manager and close function for http client instead of using `__del__` method)
  ([#99](https://github.com/tomplus/kubernetes_asyncio/pull/99), [@jnschaeffer](https://github.com/jnschaeffer))

# v11.1.0

* feat: add compatability for follow methods ([#98](https://github.com/tomplus/kubernetes_asyncio/pull/98), [@playground-julia](https://github.com/playground-julia))

# v11.0.0

* feat: regenerate library using the latest version of openapi-generator (4.3.x) ([gen/#146](https://github.com/kubernetes-client/gen/pull/146), [@tomplus](https://github.com/tomplus))
* test: add tests for Python 3.8. ([#86](https://github.com/tomplus/kubernetes_asyncio/pull/86), [@tomplus](https://github.com/tomplus))
* fix: prevent installing aiohttp 4.0 and up for now ([#88](https://github.com/tomplus/kubernetes_asyncio/pull/88), [@sepulworld](https://github.com/sepulworld))
* fix: watch.stream stores resource_version for the next call ([#89](https://github.com/tomplus/kubernetes_asyncio/pull/89), [@tomplus](https://github.com/tomplus))
* chore: remove unused path import ([#92](https://github.com/tomplus/kubernetes_asyncio/pull/92), [@aK0nshin](https://github.com/aK0nshin))

**API Change:**
- Introduce `ExtensionsV1beta1RuntimeClassStrategyOptions` and `PolicyV1beta1RuntimeClassStrategyOptions`. Add RuntimeClass restrictions & defaulting to PodSecurityPolicy [kubernetes/kubernetes#73795](https://github.com/kubernetes/kubernetes/pull/73795)
- Introduce `V1WindowsSecurityContextOptions`. Add Windows specific options in Pod Security Context and Container Security Context [kubernetes/kubernetes#77147](https://github.com/kubernetes/kubernetes/pull/77147)
- Split `V1beta1Webhook` into `V1beta1MutatingWebhook` and `V1beta1ValidatingWebhook` [kubernetes/kubernetes#78491](https://github.com/kubernetes/kubernetes/pull/78491)
- Introduce parameter `allow_watch_bookmarks` in list options for requesting watch bookmarks from apiserver. The implementation in apiserver is hidden behind feature gate `WatchBookmark` (currently in Alpha stage) [kubernetes/kubernetes#74074](https://github.com/kubernetes/kubernetes/pull/74074)
- Add `V1DeleteOptions` parameters (`dry_run`, `grace_period_seconds`, `orphan_dependents`, `propagation_policy`) to delete collection APIs [kubernetes/kubernetes#77843](https://github.com/kubernetes/kubernetes/pull/77843)
- Add ListMeta.RemainingItemCount. When responding a LIST request, if the server has more data available, and if the request does not contain label selectors or field selectors, the server sets the ListOptions.RemainingItemCount to the number of remaining objects [kubernetes/kubernetes#75993](https://github.com/kubernetes/kubernetes/pull/75993)
- Add `controller_expand_secret_ref` in `V1SecretReference` to store CSI volume expansion secrets [kubernetes/kubernetes#77516](https://github.com/kubernetes/kubernetes/pull/77516)
- Introduce `preemption_policy` field to V1PriorityClass [kubernetes/kubernetes#74614](https://github.com/kubernetes/kubernetes/pull/74614)
- Add `port` configuration to service reference in Admission webhook configuration, AuditSink webhook configuration, CRD Conversion webhook configuration and kube-aggregator [kubernetes/kubernetes#74855](https://github.com/kubernetes/kubernetes/pull/74855)
- Introduce `inline_volume_spec` to `V1PersistentVolumeSpec` [kubernetes/kubernetes#77703](https://github.com/kubernetes/kubernetes/pull/77703)
- Add fields `x_kubernetes_embedded_resource`, `x_kubernetes_int_or_string`, `x_kubernetes_preserve_unknown_fields` to V1beta1JSONSchemaProps [kubernetes/kubernetes#77207](https://github.com/kubernetes/kubernetes/pull/77207)

# v10.0.1

* fix: when `_preload_content=False` Websocket Stream returns 401 error ([#84](https://github.com/tomplus/kubernetes_asyncio/pull/84), [@kexirong](https://github.com/kexirong))
* fix: e2e tests use `apps/v1` api instead of removed `extensions/v1beta1` ([#85](https://github.com/tomplus/kubernetes_asyncio/pull/85), [@tomplus](https://github.com/tomplus))

# v10.0.0

* feat: add `create_form_yaml()` functionality ([#76](https://github.com/tomplus/kubernetes_asyncio/pull/76), [@PidgeyBE](https://github.com/PidgeyBE))
* feat: custom objects can be merged by json-patch ([gen/#119](https://github.com/kubernetes-client/gen/pull/119), [@tomplus](https://github.com/tomplus)) 
* fix: parse microseconds in data-time fields ([#80](https://github.com/tomplus/kubernetes_asyncio/pull/80), [@tomplus](https://github.com/tomplus))
* feat: upgrade to API spec from Kubernetes 1.14 ([#83](https://github.com/tomplus/kubernetes_asyncio/pull/83), [@tomplus](https://github.com/tomplus))

**API Change:**

- Remove the AdmissionregistrationV1alpha1 API group, containing only the InitializationConfiguration type [kubernetes/kubernetes#72972](https://github.com/kubernetes/kubernetes/pull/72972)
- Promote Lease API to v1 [kubernetes/kubernetes#72239](https://github.com/kubernetes/kubernetes/pull/72239)
- The Ingress API is now available via `NetworkingV1beta1Api`. `ExtensionsV1beta1Api` Ingress objects are deprecated and will no longer be served in Kubernetes v1.18 [kubernetes/kubernetes#74057](https://github.com/kubernetes/kubernetes/pull/74057)
- Introduce RuntimeClass to NodeV1alpha1Api and NodeV1beta1Api [kubernetes/kubernetes#74433](https://github.com/kubernetes/kubernetes/pull/74433)
- Graduate PriorityClass API to GA SchedulingV1Api [kubernetes/kubernetes#73555](https://github.com/kubernetes/kubernetes/pull/73555)
- Introduce CSINodeInfo and CSIDriver to StorageV1beta1Api [kubernetes/kubernetes#74283](https://github.com/kubernetes/kubernetes/pull/74283)
- The alpha Initializers feature, `admissionregistration.k8s.io/v1alpha1` API version, `Initializers` admission plugin, and use of the `metadata.initializers` API field have been removed. Discontinue use of the alpha feature and delete any existing `InitializerConfiguration` API objects before upgrading. The `metadata.initializers` field will be removed in a future release. The parameter `include_uninitialized` has been removed. [kubernetes/kubernetes#72972](https://github.com/kubernetes/kubernetes/pull/72972)

# v9.1.0

* feat: check whether an object key is present on watch ([#71](https://github.com/tomplus/kubernetes_asyncio/pull/71), [@mickours](https://github.com/mickours))
* feat: merging kubeconfig files ([#69](https://github.com/tomplus/kubernetes_asyncio/pull/69), [@tomplus](https://github.com/tomplus))

# v9.0.0

* feat: switch to openapi-generator ([#58](https://github.com/tomplus/kubernetes_asyncio/pull/58), [@tomplus](https://github.com/tomplus))
* feat: add fieldSelector parameter to list/watch methods in custom objects spec ([gen/#106](https://github.com/kubernetes-client/gen/pull/106))
* feat: upgrade to API spec from Kubernetes 1.13 ([#58](https://github.com/tomplus/kubernetes_asyncio/pull/58), [@tomplus](https://github.com/tomplus))

Breaking Changes:
* Model v1beta1WebhookClientConfig is renamed to AdmissionregistrationV1beta1WebhookClientConfig, to avoid naming conflict
   with ApiextensionsV1beta1WebhookClientConfig introduced in: kubernetes/kubernetes#67006
* Delete request's body parameter is optional kubernetes/kubernetes#70032

# v8.1.0

* feat: watch improvement (context manager, close method) ([#61](https://github.com/tomplus/kubernetes_asyncio/pull/61), [@hubo1016](https://github.com/hubo1016))

# v8.0.3

* fix: use `yaml.safe_load`, `yaml.safe_dump` for security reasons ([#57](https://github.com/tomplus/kubernetes_asyncio/pull/57), [@tomplus](https://github.com/tomplus))

# v8.0.2

* feat: remove dependency to urllib3 from kube_config, pin urlllib>=1.23 due to CVE-2018-20060 ([#56](https://github.com/tomplus/kubernetes_asyncio/pull/56), [@tomplus](https://github.com/tomplus))

# v8.0.1

* fix: kubeconfig loading failure when server uri contains trailing slash ([#53](https://github.com/tomplus/kubernetes_asyncio/pull/53), [@tomplus](https://github.com/tomplus))
* feat: regenerate client with thread-pool optimization ([#54](https://github.com/tomplus/kubernetes_asyncio/pull/54), [@tomplus](https://github.com/tomplus))

# v8.0.0

* feat: upgrade to API spec from Kubernetes 1.12 ([#50](https://github.com/tomplus/kubernetes_asyncio/pull/50), [@tomplus](https://github.com/tomplus))

# v7.0.0

* first stable release 7.0.0

# v1.0.0-beta9

* fix: option verify-ssl impacts on server certs only ([#46](https://github.com/tomplus/kubernetes_asyncio/pull/46),
  [@tomplus](https://github.com/tomplus))

# v1.0.0-beta8

* feat: add debug logs to KubeConfigLoader ([#45](https://github.com/tomplus/kubernetes_asyncio/pull/45),
  [@tomplus](https://github.com/tomplus))
* feat: exec-plugins support in kubeconfig ([#44](https://github.com/tomplus/kubernetes_asyncio/pull/44),
  [@tomplus](https://github.com/tomplus))
* fix: read config data with bytes (python3) ([#41](https://github.com/tomplus/kubernetes_asyncio/pull/41),
  [@tomplus](https://github.com/tomplus))

# v1.0.0-beta7

* feat: add OIDC auth support ([#36](https://github.com/tomplus/kubernetes_asyncio/pull/36),
  [@bpicolo](https://github.com/bpicolo))

# v1.0.0-beta6

* feat: regenerate with latest client gen to get custom object status scale api
  ([#37](https://github.com/tomplus/kubernetes_asyncio/pull/37), [@juliantaylor](https://github.com/juliantaylor))
* fix: handling timeout by watch loop ([#39](https://github.com/tomplus/kubernetes_asyncio/pull/39),
  [@tomplus](https://github.com/tomplus))

# v1.0.0-beta5

* feat: upgrade to spec from Kuberentes 1.11 ([#34](https://github.com/tomplus/kubernetes_asyncio/pull/34), [@tomplus](https://github.com/tomplus))

# v1.0.0-beta4

* fix: aiohttp with `verify_ssl=False` ([#33](https://github.com/tomplus/kubernetes_asyncio/pull/33), [@bpicolo](https://github.com/bpicolo))

# v1.0.0-beta3

* feat: watch work forever if timeout is not specified ([#30](https://github.com/tomplus/kubernetes_asyncio/pull/30), [@tomplus](https://github.com/tomplus))

# v1.0.0-beta2

* feat: support Python 3.7 ([#28](https://github.com/tomplus/kubernetes_asyncio/pull/28), [@tomplus](https://github.com/tomplus))

# v1.0.0-beta1

* feat: make function `load_kube_config` asynchronous
* feat: function to auto-refresh gke token 
* feat: remove synchronous libraries from dependencies

# v1.0.0-alpha4

* feat: watch stops the iterator for empty responses and do not process ERROR responses ([#22](https://github.com/tomplus/kubernetes_asyncio/pull/22), [@olitheolix](https://github.com/olitheolix))
* feat: replace urllib3 by http.client in e2e initializer ([#20](https://github.com/tomplus/kubernetes_asyncio/pull/20), [@tomplus](https://github.com/tomplus))
* feat: new example - tail.py ([#19](https://github.com/tomplus/kubernetes_asyncio/pull/19), [@tomplus](https://github.com/tomplus))
* feat: new example - simultaneously watch multiple event streams without threads ([#13](https://github.com/tomplus/kubernetes_asyncio/pull/13), [@olitheolix](https://github.com/olitheolix))
* fix: fix few typos in setup.py ([#18](https://github.com/tomplus/kubernetes_asyncio/pull/18), [@evemorgen](https://github.com/evemorgen))
* fix: requirement for requests and urllib3 version ([#16](https://github.com/tomplus/kubernetes_asyncio/pull/16), [@tomplus](https://github.com/tomplus))

# v1.0.0-alpha3

* fix e2e and unit tests
* fix Watch, Stream

# v1.0.0-alpha2

* fix requirements.txt

# v1.0.0-alpha1

* first release
