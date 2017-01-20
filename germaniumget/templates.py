from jinja2 import Template
import textwrap
from styles import text

def template_run_node(**data):
    """
    Call the run node template.
    """

    template = Template(textwrap.dedent(
    r"""
    {{java_home}}/bin/java %SELENIUM_JAVA_OPTS% -jar {{germanium_home}}/lib/selenium-standalone.jar ^
        -role node ^
        -hub http://{{hub_address}}/grid/register ^
        -nodeConfig {{germanium_home}}/germanium-node.conf ^
        %SELENIUM_OPTS%
    """).strip())

    return template.render(**data)


def template_configuration_file(**data):
    """
    Call the configuration file template.
    """

    template = Template(textwrap.dedent(
    r"""
    {
      "capabilities": [
        {% for browser in browsers %}{
          "browserName": "{{browser.browserName}}",
          "maxInstances": {{browser.maxInstances}},
          "seleniumProtocol": "{{browser.seleniumProtocol}}"
        }{% if not loop.last %},{% endif %}{% endfor %}
      ],
      "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
      "maxSession": 20,
      "port": 5555,
      "register": true,
      "registerCycle": 5000
    }
    """).strip())

    return template.render(**data)


def write_file(file_name, string_data):
    with open(file_name, "w") as text_file:
        text_file.write(string_data)
    print(text("Wrote %s." % file_name))

