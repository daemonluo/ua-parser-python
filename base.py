#coding=utf8

import re

from MANUFACTURER import *

class UserAgent(object):
    def __init__(self):
        self.os = {
            'name' : None,
            'version' : None,
        }
        self.engine = {
            'name' : None,
            'version' : None,
        }
        self.browser = {
            'name' : None,
            'version' : None,
            'mode' : '',
        }
        self.device = {
            'model' : None,
            'manufacturer' : None,
            'category' : None,
        }

    def __repr__(self):
        return str(self.to_object())
        return self.pretty()

    def set_os(self, os):
        if not isinstance(os, dict):
            return
        if os.get('name', None):
            self.os['name'] = os.get('name', '').strip('- ')
        else:
            self.os['name'] = ''

        if os.has_key('version'):
            if isinstance(os['version'], dict):
                if os['version'].get('alias', None):
                    self.os['version'] = os['version']['alias']
                elif os['version'].get('original', None):
                    self.os['version'] = os['version']['original']
                elif os['version'].get('value', None):
                    self.os['version'] = os['version']['value']
                else:
                    self.os['version'] = ''
            elif isinstance(os['version'], str):
                self.os['version'] = os['version']
            else:
                self.os['version'] = ''
        else:
            self.os['version'] = ''

    def set_engine(self, engine):
        if not isinstance(engine, dict):
            return
        if engine.get('name', None):
            self.engine['name'] = engine.get('name', '').strip('- ')
        else:
            self.engine['name'] = ''

        if engine.has_key('version'):
            if isinstance(engine['version'], dict):
                if engine['version'].get('alias', None):
                    self.engine['version'] = engine['version']['alias']
                elif engine['version'].get('original', None):
                    self.engine['version'] = engine['version']['original']
                elif engine['version'].get('value', None):
                    self.engine['version'] = engine['version']['value']
                else:
                    self.engine['version'] = ''
            elif isinstance(engine['version'], str):
                self.engine['version'] = engine['version']
            else:
                self.engine['version'] = ''
        else:
            self.engine['version'] = ''

    def set_browser(self, browser):
        if not isinstance(browser, dict):
            return
        if browser.get('name', None):
            self.browser['name'] = browser.get('name', '').strip('- ')
        else:
            self.browser['name'] = ''
        if browser.has_key('version'):
            if isinstance(browser['version'], dict):
                if browser['version'].get('alias', None):
                    self.browser['version'] = browser['version']['alias']
                elif browser['version'].get('original', None):
                    self.browser['version'] = browser['version']['original']
                elif browser['version'].get('value', None):
                    self.browser['version'] = browser['version']['value']
                else:
                    self.browser['version'] = ''
            elif isinstance(browser['version'], str):
                self.browser['version'] = browser['version']
            else:
                self.browser['version'] = ''
        else:
            self.browser['version'] = ''
        if browser.get('mode', None):
            self.browser['mode'] = browser.get('mode', '').strip('- ')
        else:
            self.browser['mode'] = ''

    def set_device(self, device):
        if not isinstance(device, dict):
            return
        for attr in ['model', 'manufacturer', 'category']:
            if device.get(attr, None):
                self.device[attr] = device[attr].strip('- ')
            else:
                self.device[attr] = ''

    def pretty(self):
        output = '{\n'
        indent = '    '

        output += indent + '"' + 'os' + '" : {\n'
        output += indent * 2 + '"name" : "' + self.os['name'] + '",\n'
        output += indent * 2 + '"version" : "' + self.os['version'] + '"\n'
        output += indent + '},\n'
        
        output += indent + '"' + 'engine' + '" : {\n'
        output += indent * 2 + '"name" : "' + self.engine['name'] + '",\n'
        output += indent * 2 + '"version" : "' + self.engine['version'] + '"\n'
        output += indent + '},\n'

        output += indent + '"browser" : {\n'
        output += indent * 2 + '"name" : "' + self.browser['name'] + '",\n'
        output += indent * 2 + '"version" : "' + self.browser['version'] + '",\n'
        output += indent * 2 + '"mode" : "' + self.browser['mode'] + '"\n'
        output += indent + '},\n'

        output += indent + '"device" : {\n'
        output += indent * 2 + '"category" : "' + self.device['category'] + '",\n'
        output += indent * 2 + '"model" : "' + self.device['model'] + '",\n'
        output += indent * 2 + '"manufacturer" : "' + self.device['manufacturer'] + '"\n'
        output += indent + '}\n'

        output += '}'
        return output;

    def compact(self):
        output = ''
        output += 'name=%s,version=%s;' % (self.os['name'], self.os['version'])
        output += 'name=%s,version=%s;' % (self.engine['name'], self.engine['version'])
        output += 'name=%s,version=%s,mode=%s;' % (self.browser['name'], self.browser['version'], self.browser['mode'])
        output += 'model=%s,manufacturer=%s,category=%s' % (self.device['model'], self.device['manufacturer'], self.device['category'])

        return output;

    def to_object(self):
        return {
            'os' : self.os,
            'engine' : self.engine,
            'browser' : self.browser,
            'device' : self.device
        }

    def equals(self, user_agent):
        if not isinstance(user_agent, UserAgent):
            return False
        return self.os['name'] == user_agent.os['name'] and self.os['version'] == user_agent.os['version'] and self.engine['name'] == user_agent.engine['name'] and self.engine['version'] == user_agent.engine['version'] and self.browser['name'] == user_agent.browser['name'] and self.browser['version'] == user_agent.browser['version'] and self.browser['mode'] == user_agent.browser['mode'] and self.device['model'] == user_agent.device['model'] and self.device['manufacturer'] == user_agent.device['manufacturer'] and self.device['category'] == user_agent.device['category']

class UA(object):
    def __init__(self, ua, **kargs):
        self.ua = ua
        self.os = {
            'name' : None,
            'version' : {
                'value' : None
            },
        }
        self.engine = {
            'name' : None,
            'version' : {
                'value' : None
            },
        }
        self.browser = {
            'name' : None,
            'version' : {
                'value' : None
            },
            'mode' : '',
        }
        self.device = {
            'model' : None,
            'manufacturer' : None,
            'category' : None,
        }
        self.camouflage = kargs.pop('camouflage', False)
        self.useFeatures = False
        self.detect_camouflage = True

    def parse_version(self, version):
        components = version.split('.')
        if len(components) == 0:
            return 0.0
        major = components.pop(0)
        if len(components) == 0:
            return float(major)

        version = '%s.%s' % (major, ''.join(components))
        return float(version)

    def cleanup_model(self, model):
        if model is None:
            model = ''
        model = re.sub(r'_TD$', '', model)
        model = re.sub(r'_CMCC$', '', model)

        model = re.sub(r'_', ' ', model)
        model = re.sub(r'^\s+|\s+$', '', model)
        model = re.sub(r'/[^/]+$', '', model)
        model = re.sub(r'/[^/]+ Android/.*', '', model)

        model = re.sub(r'^tita on ', '', model)
        model = re.sub(r'^Android on ', '', model)
        model = re.sub(r'^Android for ', '', model)
        model = re.sub(r'^ICS AOSP on ', '', model)
        model = re.sub(r'^Full AOSP on ', '', model)
        model = re.sub(r'^Full Android on ', '', model)
        model = re.sub(r'^Full Cappuccino on ', '', model)
        model = re.sub(r'^Full MIPS Android on ', '', model)
        model = re.sub(r'^Full Android', '', model)

        model = re.sub(re.compile(r'^Acer ?', re.I), '', model)
        model = re.sub(r'^Iconia ', '', model)
        model = re.sub(r'^Ainol ', '', model)
        model = re.sub(re.compile(r'^Coolpad ?', re.I), 'Coolpad ', model)
        model = re.sub(r'^ALCATEL ', '', model)
        model = re.sub(r'^Alcatel OT-(?P<match>.*)', lambda m:'one touch %s' % m.group('match'), model)
        model = re.sub(r'^YL-', '', model)
        model = re.sub(r'^Novo7 ?', 'Novo7 ', model, re.I)
        model = re.sub(r'^GIONEE ', '', model)
        model = re.sub(r'^HW-', '', model)
        model = re.sub(re.compile(r'^Huawei[-\s]', re.I), 'Huawei ', model)
        model = re.sub(re.compile(r'^SAMSUNG[- ]', re.I), '', model)
        model = re.sub(r'^SonyEricsson', '', model)
        model = re.sub(r'^Lenovo Lenovo', 'Lenovo', model)
        model = re.sub(r'^LNV-Lenovo', 'Lenovo', model)
        model = re.sub(r'^Lenovo-', 'Lenovo ', model)
        model = re.sub(r'^(LG)[ _/]', 'LG-', model)
        model = re.sub(r'^(?P<manufacturer>HTC.*)\s(?:v|V)?[0-9.]+$', lambda m:m.group('manufacturer'), model)
        model = re.sub(r'^(HTC)[-/]', 'HTC ', model)
        model = re.sub(r'^(?P<match1>HTC)(?P<match2>[A-Z][0-9][0-9][0-9])', lambda m:'%s %s' % (m.group('match1'), m.group('match2')), model)
        model = re.sub(r'^(Motorola[\s|-])', '', model)
        model = re.sub(r'^(Moto|MOT-)', '', model)

        model = re.sub(re.compile(r'-?(orange(-ls)?|vodafone|bouygues)$', re.I), '', model)
        model = re.sub(re.compile(r'http://.+$', re.I), '', model)

        model = re.sub(r'^\s+|\s+$', '', model)

        return model

    def _parse_os_and_device(self):
        # Unix
        if 'Unix' in self.ua:
            self.os['name'] = 'Unix'

        if 'FreeBSD' in self.ua:
            self.os['name'] = 'FreeBSD'

        if 'OpenBSD' in self.ua:
            self.os['name'] = 'OpenBSD'

        if 'NetBSD' in self.ua:
            self.os['name'] = 'NetBSD'

        if 'SunOS' in self.ua:
            self.os['name'] = 'Solaris'

        # Linux
        if 'Linux' in self.ua:
            self.os['name'] = 'Linux'

            if 'CentOS' in self.ua:
                self.os['name'] = 'CentOS'
                match = re.search(r'CentOS/[0-9\.\-]+el([0-9_]+)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1).replace('_', '.')

            if 'Debian' in self.ua:
                self.os['name'] = 'Debian'

            if 'Fedora' in self.ua:
                self.os['name'] = 'Fedora'
                match = re.search(r'Fedora/[0-9\.\-]+fc([0-9]+)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1)

            if 'Gentoo' in self.ua:
                self.os['name'] = 'Gentoo'

            if 'Kubuntu' in self.ua:
                self.os['name'] = 'Kubuntu'
            
            if 'Mandriva Linux' in self.ua:
                self.os['name'] = 'Mandriva'
                match = re.search(r'Mandriva Linux/[0-9\.\-]+mdv([0-9]+)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1)
            
            if 'Mageia' in self.ua:
                self.os['name'] = 'Mageia'
                match = re.search(r'Mageia/[0-9\.\-]+mga([0-9]+)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1)

            if 'Red Hat' in self.ua:
                self.os['name'] = 'Red Hat'
                match = re.search(r'Red Hat[^/]*/[0-9\.\-]+el([0-9_]+)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1).replace('_', '.')

            if 'Slackware' in self.ua:
                self.os['name'] = 'Slackware'

            if 'SUSE' in self.ua:
                self.os['name'] = 'SUSE'

            if 'Turbolinux' in self.ua:
                self.os['name'] = 'Turbolinux'

            if 'Ubuntu' in self.ua:
                self.os['name'] = 'Ubuntu'
                match = re.search(r'Ubuntu/([0-9.]*)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1)

        # IOS
        if re.search(r'iPhone( Simulator)?;', self.ua) or 'iPad;' in self.ua or 'iPod;' in self.ua:
            self.os['name'] = 'iOS'
            self.os['version']['value'] = '1.0'

            match = re.search(r'OS (.*) like Mac OS X', self.ua)
            if match:
                self.os['version']['value'] = match.group(1).replace('_', '.')
            
            if 'iPhone Simulator;' in self.ua:
                self.device['type'] = 'emulator'
            elif 'iPod;' in self.ua:
                self.device['type'] = 'media'
                self.device['manufacturer'] = 'Apple'
                self.device['model'] = 'iPod Touch'
            elif 'iPhone;' in self.ua:
                self.device['type'] = 'mobile'
                self.device['manufacturer'] = 'Apple'
                self.device['model'] = 'iPhone'
            else:
                self.device['type'] = 'tablet'
                self.device['manufacturer'] = 'Apple'
                self.device['model'] = 'iPad'

            self.device['identified'] = True
        elif 'Mac OS X' in self.ua: # MacOS X
            self.os['name'] = 'Mac OS X'
            match = re.search(r'Mac OS X (10[0-9\._]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1).replace('_', '.')
                self.os['version'] = Version({'value':match.group(1).replace('_', '.')})

        # Windows
        if 'Windows' in self.ua:
            self.os['name'] = 'Windows'
            match = re.search(r'Windows NT ([0-9]\.[0-9])', self.ua)
            if match:
                version = match.group(1)
                self.os['version']['value'] = parse_version(version)
                if version == '6.2':
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = '8'
                elif version == '6.1':
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = '7'
                elif version == '6.0':
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = 'Vista'
                elif version == '5.2':
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = 'Server 2003'
                elif version == '5.1':
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = 'XP'
                elif version == '5.0':
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = '2000'
                else:
                    self.os['version']['value'] = version
                    self.os['version']['alias'] = 'NT ' + str(self.os['version']['value'])

            if 'Windows 95' in self.ua or 'Win95' in self.ua or 'Win 9x 4.00' in self.ua:
                self.os['version']['value'] = '4.0'
                self.os['version']['alias'] = '95'
            
            if 'Windows 98' in self.ua or 'Win98' in self.ua or 'Win 9x 4.10' in self.ua:
                self.os['version']['value'] = '4.1'
                self.os['version']['alias'] = '98'

            if 'Windows ME' in self.ua or 'WinME' in self.ua or 'Win 9x 4.90' in self.ua:
                self.os['version']['value'] = '4.9'
                self.os['version']['alias'] = 'ME'

            if 'Windows XP' in self.ua or 'WinXP' in self.ua:
                self.os['version']['value'] = '5.1'
                self.os['version']['alias'] = 'XP'

            if 'WP7' in self.ua:
                self.os['name'] = 'Windows Phone'
                self.os['version']['value'] = '7.0'
                self.os['version']['details'] = 2
                self.device['type'] = 'mobile'
                self.device['mode'] = 'desktop'

            if 'Windows CE' in self.ua or 'WinCE' in self.ua or 'WindowsCE' in self.ua:
                if ' IEMobile' in self.ua:
                    self.os['name'] = 'Windows Mobile'
                    
                    if ' IEMobile 8' in self.ua:
                        self.os['version']['value'] = '6.5'
                        self.os['version']['details'] = 2

                    if ' IEMobile 7' in self.ua:
                        self.os['version']['value'] = '6.1'
                        self.os['version']['details'] = 2

                    if ' IEMobile 6' in self.ua:
                        self.os['version']['value'] = '6.0'
                        self.os['version']['details'] = 2
                else:
                    self.os['name'] = 'Windows CE'
                    match = re.search(r'WindowsCEOS/([0-9.]*)', self.ua)
                    if match:
                        self.os['version']['value'] = match.group(1)
                        self.os['version']['details'] = 2
                    match = re.search(r'Windows CE ([0-9.]*)', self.ua)
                    if match:
                        self.os['version']['value'] = match.group(1)
                        self.os['version']['details'] = 2
                    self.device['type'] = 'mobile'

            if 'Windows Mobile' in self.ua:
                self.os['name'] = 'Windows Mobile'
                self.device['type'] = 'mobile'

            match = re.search(r'WindowsMobile/([0-9.]*)', self.ua)
            if match:
                self.os['name'] = 'Windows Mobile'
                self.os['version']['value'] = match.group(1)
                self.os['version']['details'] = 2
                self.device['type'] = 'mobile'

            match = re.search(r'Windows Phone [0-9]', self.ua)
            if match:
                self.os['name'] = 'Windows Mobile'
                self.os['version']['value'] = re.search('Windows Phone ([0-9.]*)', self.ua).group(1)
                self.os['version']['details'] = 2
                self.device['type'] = 'mobile'

            if 'Windows Phone OS' in self.ua:
                self.os['name'] = 'Windows Phone'
                self.os['version']['value'] = re.search('Windows Phone OS ([0-9.]*)', self.ua).group(1)
                self.os['version']['details'] = 2
                if int(self.os['version']['value'].split('.').pop(0)) < 7:
                    self.os['name'] = 'Windows Mobile'

                match = re.search(r'IEMobile/[^;]+; ([^;]+); ([^;]+)[;|\)]', self.ua)
                if match:
                    self.device['manufacturer'] = match.group(1)
                    self.device['model'] = match.group(2)

                self.device['type'] = 'mobile'

                manufacturer = self.device['manufacturer']
                model = self.cleanup_model(self.device['model'])

                if manufacturer in WINDOWS_PHONE_MODELS and model in WINDOWS_PHONE_MODELS[manufacturer]:
                    self.device['manufacturer'] = WINDOWS_PHONE_MODELS[manufacturer][model][0]
                    self.device.model = WINDOWS_PHONE_MODELS[manufacturer][model][1]
                    self.device['identified'] = True

                if manufacturer == 'Microsoft' and model == 'XDeviceEmulator':
                    self.device['manufacturer'] = None
                    self.device['model'] = None
                    self.device['type'] = 'emulator'
                    self.device['identified'] = True

        # Android
        if 'Android' in self.ua:
            self.os['name'] = 'Android'
            self.os['version']['value'] = None

            match = re.search(r'Android(?: )?(?:AllPhone_|CyanogenMod_)?(?:/)?v?([0-9.]+)', self.ua.replace('-update', '.'))
            if match:
                self.os['version']['value'] = match.group(1)
                self.os['version']['details'] = 3

            if 'Android Eclair' in self.ua:
                self.os['version']['value'] = '2.0'
                self.os['version']['details'] = 3

            self.device['type'] = 'mobile'
            if self.os['version']['value'] and int(self.os['version']['value'].split('.').pop(0)) >= 3:
                self.device['type'] = 'tablet'
            if self.os['version']['value'] and int(self.os['version']['value'].split('.').pop(0)) >= 4 and 'Mobile' in self.ua:
                self.device['type'] = 'mobile'

            if re.search(r'Eclair; (?:[a-zA-z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?) Build/([^/]*)/', self.ua):
                match = re.search(r'Eclair; (?:[a-zA-z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?) Build/([^/]*)/', self.ua)
                self.device['model'] = match.group(1)
            elif re.search(r'; ([^;]*[^;\s])\s+Build', self.ua):
                match = re.search(r'; ([^;]*[^;\s])\s+Build', self.ua)
                self.device['model'] = match.group(1)
            elif re.search(r'[a-zA-Z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?; ([^;]*[^;]*[^;\s]);\s+Build', self.ua):
                match = re.search(r'[a-zA-Z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?; ([^;]*[^;]*[^;\s]);\s+Build', self.ua)
                self.device['model'] = match.group(1)
            elif re.search(r'\(([^;]+);U;Android/[^;]+;[0-9]+\*[0-9]+;CTC/2.0\)', self.ua):
                match = re.search(r'\(([^;]+);U;Android/[^;]+;[0-9]+\*[0-9]+;CTC/2.0\)', self.ua)
                self.device['model'] = match.group(1)
            elif re.search(r';\s?([^;]+);\s?[0-9]+\*[0-9]+;\s?CTC/2.0', self.ua):
                match = re.search(r';\s?([^;]+);\s?[0-9]+\*[0-9]+;\s?CTC/2.0', self.ua)
                self.device['model'] = match.group(1)
            elif re.search(r'zh-cn;\s*(.*?)(/|build)/', self.ua, re.IGNORECASE):
                match = re.search(r'zh-cn;\s*(.*?)(/|build)/', self.ua, re.IGNORECASE)
                self.device['model'] = match.group(1)
            elif re.search(r'Android [^;]+; (?:[a-zA-Z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?; )?([^)]+)\)', self.ua):
                match = re.search(r'Android [^;]+; (?:[a-zA-Z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?; )?([^)]+)\)', self.ua)
                if not re.search(r'[a-zA-Z][a-zA-Z](?:[-_][a-zA-Z][a-zA-Z])?', self.ua):
                    self.device['model'] = match.group(1)
            elif re.search(r'(.+?)/\S+', self.ua, re.IGNORECASE):
                match = re.search(r'^(.+?)/\S+', self.ua, re.IGNORECASE)
                self.device['model'] = match.group(1)

            # Sometimes we get a model name that starts with Android, in that case it is mismatch and we should ignore it
            if self.device.get('model', False) and self.device['model'].startswith('Android'):
                self.device['model'] = None
            if self.device.get('model', False):
                model = self.cleanup_model(self.device['model'])
                if model in ANDROID_MODELS:
                    self.device['manufacturer'] = ANDROID_MODELS[model][0]
                    self.device['model'] = ANDROID_MODELS[model][1]
                    if len(ANDROID_MODELS[model]) > 2:
                        self.device['type'] = ANDROID_MODELS[model][2]
                    self.device['identified'] = True

                if model in ['Emulator', 'x86 Emulator', 'x86 VirtualBox', 'vm']:
                    self.device['manufacturer'] = None
                    self.device['model'] = None
                    self.device['type'] = 'emulator'
                    self.device['identified'] = True

            if 'HP eStation' in self.ua:
                self.device['manufacturer'] = 'HP'
                self.device['model'] = 'eStation'
                self.device['type'] = 'tablet'
                self.device['identified'] = True

            if 'Pre/1.0' in self.ua:
                self.device['manufacturer'] = 'Palm'
                self.device['model'] = 'Pre'
                self.device['identified'] = True

            if 'Pre/1.1' in self.ua:
                self.device['manufacturer'] = 'Palm'
                self.device['model'] = 'Pre Plus'
                self.device['identified'] = True

            if 'Pre/1.2' in self.ua:
                self.device['manufacturer'] = 'Palm'
                self.device['model'] = 'Pre 2'
                self.device['identified'] = True

            if 'Pre/3.0' in self.ua:
                self.device['manufacturer'] = 'HP'
                self.device['model'] = 'Pre 3'
                self.device['identified'] = True

            if 'Pixi/1.0' in self.ua:
                self.device['manufacturer'] = 'Palm'
                self.device['model'] = 'Pixi'
                self.device['identified'] = True

            if 'Pixi/1.1' in self.ua:
                self.device['manufacturer'] = 'Palm'
                self.device['model'] = 'Pixi Plus'
                self.device['identified'] = True

            if 'P160UN/1.0' in self.ua:
                self.device['manufacturer'] = 'HP'
                self.device['model'] = 'Veer'
                self.device['identified'] = True

        # Google TV
        if 'GoogleTV' in self.ua:
            self.os['name'] = 'Google TV'

            if 'Chrome/5.' in self.ua:
                self.os['version']['value'] = '1'

            if 'Chrome/11.' in self.ua:
                self.os['version']['value'] = '2'

            self.device['type'] = 'television'

        # WoPhone
        if 'WoPhone' in self.ua:
            self.os['name'] = 'WoPhone'
            match = re.search(r'WoPhone/([0-9\.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)
            self.device['type'] = 'mobile'

        # BlackBerry
        if 'BlackBerry' in self.ua:
            self.os['name'] = 'BlackBerry OS'

            if not 'Opera' in self.ua:
                match = re.search(r'BlackBerry([0-9]*)/([0-9.]*)', self.ua)
                if match:
                    self.device['model'] = match.group(1)
                    self.os['version']['value'] = match.group(2)
                    self.os['version']['details'] = 2

                match = re.search(r'; BlackBerry ([0-9]*);', self.ua)
                if match:
                    self.device['model'] = match.group(1)

                match = re.search(r'Version/([0-9.]*)', self.ua)
                if match:
                    self.os['version']['value'] = match.group(1)
                    self.os['version']['details'] = 2

                if self.os['version']['value'] and int(self.os['version']['value'].split('.').pop(0)) >= 10:
                    self.os['name'] = 'BlackBerry'

                if 'model' in self.device:
                    if self.device['model'] in BLACKBERRY_MODELS:
                        self.device['model'] = 'BlackBerry ' + BLACKBERRY_MODELS[self.device['model']] + ' ' + self.device['model']
                    else:
                        self.device['model'] = 'BlackBerry ' + self.device['model']
                else:
                    self.device['model'] = 'BlackBerry'

                self.device['manufacturer'] = 'RIM'
                self.device['type'] = 'mobile'
                self.device['identified'] = True
        # BlackBerry PlayBook
        if 'RIM Tablet OS' in self.ua:
            self.os['name'] = 'BlackBerry Tablet OS'
            self.os['version']['value'] = re.search(r'RIM Tablet OS ([0-9.]*)', self.ua).group(1)
            self.os['version']['details'] = 2
            self.device['manufacturer'] = 'RIM'
            self.device['model'] = 'BlackBerry PlayBook'
            self.device['type'] = 'tablet'
            self.device['identified'] = True
        elif 'PlayBook' in self.ua:
            match = re.search(r'Version/(10[0-9.]*)', self.ua)
            if match:
                self.os['name'] = 'BlackBerry'
                self.os['version']['value'] = match.group(1)
                self.os['version']['details'] = 2
                self.device['manufacturer'] = 'RIM'
                self.device['model'] = 'BlackBerry PlayBook'
                self.device['type'] = 'tablet'
                self.device['identified'] = True

        # WebOS
        if re.search(r'(?:web|hpw)OS', self.ua):
            self.os['name'] = 'webOS'
            self.os['version']['value'] = re.search(r'(?:web|hpw)OS/([0-9.]*)', self.ua).group(1)
            if 'tablet' in self.ua:
                self.device['type'] = 'tablet'
            else:
                self.device['type'] = 'mobile'

            self.device['manufacturer'] = 'HP' if 'hpwOS' in self.ua else 'Palm'
            if 'Pre/1.0' in self.ua:
                self.device['model'] = 'Pre'
            if 'Pre/1.1' in self.ua:
                self.device['model'] = 'Pre Plus'
            if 'Pre/1.2' in self.ua:
                self.device['model'] = 'Pre2'
            if 'Pre/3.0' in self.ua:
                self.device['model'] = 'Pre3'
            if 'Pixi/1.0' in self.ua:
                self.device['model'] = 'Pixi'
            if 'Pixi/1.1' in self.ua:
                self.device['model'] = 'Pixi Plus'
            if re.search(r'P160UN?A?/1.0', self.ua):
                self.device['model'] = 'Veer'
            if 'TouchPad/1.0' in self.ua:
                self.device['model'] = 'TouchPad'
            
            if 'Emulator/' in self.ua and 'Desktop/' in self.ua:
                self.device['type'] = 'emulator'
                self.device['manufacturer'] = None
                self.device['model'] = None

            self.device['identified'] = True

        # S60
        if 'Symbian' in self.ua or 'S60' in self.ua or re.search(r'Series[ ]?60', self.ua):
            self.os['name'] = 'Series60'

            if 'SymbianOS/9.1' in self.ua and 'Series60' not in self.ua:
                self.os['version']['value'] = '3.0'

            match = re.search(r'Series60/([0-9.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)

            match = re.search(r'Nokia([^/;]+)[/|;]', self.ua)
            if match:
                if match.group(1) != 'Browser':
                    self.device['manufacturer'] = 'Nokia'
                    self.device['model'] = match[1]
                    self.device['identified'] = True
            match = re.search(r'Vertu([^/;]+)[/|;]', self.ua)
            if match:
                self.device['manufacturer'] = 'Vertu'
                self.device['model'] = match.group(1)
                self.device['identified'] = True

            match = re.search(r'/Symbian; U; ([;]+); [a-z][a-z]\-[a-z][a-z]', self.ua, re.I)
            if match:
                self.device['manufacturer'] = 'Nokia'
                self.device['model'] = match.group(1)
                self.device['identified'] = True

            match = re.search(r'Samsung/([^;]*);', self.ua)
            if match:
                self.device['manufacturer'] = STRINGS_SAMSUNG
                self.device['model'] = match.group(1)
                self.device['identified'] = True

            self.device['type'] = 'mobile'

        # S40
        if 'Series40' in self.ua:
            self.os['name'] = 'Series40'
            match = re.search(r'Nokia([^/]+)/', self.ua)
            if match:
                self.device['manufacturer'] = 'Nokia'
                self.device['model'] = match.group(1)
                self.device['identified'] = True
            self.device['type'] = 'mobile'

        # MeeGo
        if 'MeeGo' in self.ua:
            self.os['name'] = 'MeeGo'
            self.device['type'] = 'mobile'

            match = re.search(r'Nokia([^\)]+)\)', self.ua)
            if match:
                self.device['manufacturer'] = 'Nokia'
                self.device['model'] = match.group(1)
                self.device['identified'] = True

        # Maemo
        if 'Maemo' in self.ua:
            self.os['name'] = 'Maemo'
            self.device['type'] = 'mobile'
            
            match = re.search(r'(N[0-9]+)', self.ua)
            if match:
                self.device['manufacturer'] = 'Nokia'
                self.device['model'] = match.group(1)
                self.device['identified'] = True

        # Tizen
        if 'Tizen' in self.ua:
            self.os['name'] = 'Tizen'
            match = re.search(r'Tizen[\/ ]([0-9.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)
            self.device['type'] = 'Mobile'
            match = re.search(r'\(([^;]+); ([^/]+)/', self.ua)
            if match:
                if match.group(1) != 'Linux':
                    self.device['manufacturer'] = match.group(1)
                    self.device['model'] = match.group(2)
                    if self.device['manufacturer'] in TIZEN_MODELS and self.device['model'] in TIZEN_MODELS[self.device['manufacturer']]:
                        manufacturer = self.device['manufacturer']
                        model = self.cleanup_model(self.device['model'])

                        self.device['manufacturer'] = TIZEN_MODELS[manufacturer][model][0]
                        self.device['model'] = TIZEN_MODELS[manufacturer][model][1]
                        self.device['identified'] = True

        # Bada
        if 'Bada' in self.ua or 'bada' in self.ua:
            self.os['name'] = 'Bada'
            match = re.search(r'[b|B]ada/([0-9.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)
            self.device['type'] = 'mobile'
            match = re.search(r'\(([^;]+); ([^/]+)/', self.ua)
            if match:
                self.device['manufacturer'] = match.group(1)
                self.device['model'] = self.cleanup_model(match.group(2))

            if BADA_MODELS.get(self.device.get('manufacturer', None), False) and BADA_MODELS[self.device.get('manufacturer', None)].get(self.device.get('model', None), False):
                manufacturer = self.device.get('manufacturer', None)
                model = self.device.get('model', None)
                self.device['manufacturer'] = BADA_MODELS[manufacturer][model][0]
                self.device['model'] = BADA_MODELS[manufacturer][model][1]
                self.device['identified'] = True

        # Brew
        if 'brew' in self.ua.lower() or 'BMP; U' in self.ua:
            self.os['name'] = 'Brew'
            self.device['type'] = 'mobile'

            if re.search(r'BREW; U; ([0-9.]*)', self.ua):
                match = re.search(r'BREW; U; ([0-9.]*)', self.ua)
                self.os['version']['value'] = match.group(1)
            elif re.search(r';BREW/([0-9.]*)', self.ua, re.I):
                match = re.search(r';BREW/([0-9.]*)', self.ua, re.I)
                self.os['version']['value'] = match.group(1)

            match = re.search(r'\(([^;]+);U;REX/[^;]+;BREW/[^;]+;(?:.*;)?[0-9]+\*[0-9]+;CTC/2.0\)', self.ua)
            if match:
                self.device['model'] = match.group(1)

            if self.device.get('model', False):
                model = self.cleanup_model(self.device['model'])
                if model in BREW_MODELS:
                    self.device['manufacturer'] = BREW_MODELS[model][0]
                    self.device['model'] = BREW_MODELS[model][1]
                    self.device['identified'] = True

        # MTK
        if re.search(r'\(MTK;', self.ua):
            self.os['name'] = 'MTK'
            self.device['type'] = 'mobile'

        # CrOS
        if 'CrOS' in self.ua:
            self.os['name'] = 'Chrome OS'
            self.device['type'] = 'desktop'

        # Joli OS
        if 'Joli OS' in self.ua:
            self.os['name'] = 'Joli OS'
            self.device['type'] = 'desktop'
            match = re.search(r'Joli OS/([0-9.]*)', self.ua, re.I)
            if match:
                self.os['version']['value'] = match.group(1)

        # Haiku
        if 'Haiku' in self.ua:
            self.os['name'] = 'Haiku'
            self.device['type'] = 'desktop'

        # QNX
        if 'QNX' in self.ua:
            self.os['name'] = 'QNX'
            self.device['type'] = 'mobile'

        # OS/2 Warp
        if 'OS/2; Warp' in self.ua:
            self.os['name'] = 'OS/2 Warp'
            self.device['type'] = 'desktop'

            match = re.search(r'OS/2; Warp ([0-9.]*)', self.ua, re.I)
            if match:
                self.os['version']['value'] = match.group(1)

        # Grid OS
        if 'Grid OS' in self.ua:
            self.os['name'] = 'Grid OS'
            self.device['type'] = 'tablet'

            match = re.search(r'Grid OS ([0-9.]*)', self.ua, re.I)
            if match:
                self.os['version']['value'] = match.group(1)

        # AmigaOS
        if 'AmigaOS'.lower() in self.ua.lower():
            self.os['name'] = 'AmigaOS'
            self.os['type'] = 'desktop'

            match = re.search(r'AmigaOS ([0-9.]*)', self.ua, re.I)
            if match:
                self.os['version']['value'] = match.group(1)

        # MorphOS
        if 'MorphOS'.lower() in self.ua.lower():
            self.os['name'] = 'MorphOS'
            self.device['type'] = 'desktop'

            match = re.search(r'MorphOS ([0-9.]*)', self.ua, re.I)
            self.os['version']['value'] = match.group(1)

        # Kindle
        if 'Kindle' in self.ua and 'Fire' not in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Amazon'
            self.device['model'] = 'Kindle'
            self.device['type'] = 'ereader'
            if 'Kindle/2.0' in self.ua:
                self.device['model'] = 'Kindle 2'
            if 'Kindle/3.0' in self.ua:
                self.device['model'] = 'Kindle 3 or later'
            self.device['identified'] = True

        # NOOK
        if 'nook browser' in self.ua:
            self.os['name'] = 'Android'
            self.device['manufacturer'] = 'Barnes & Noble'
            self.device['model'] = 'NOOK'
            self.device['type'] = 'ereader'
            self.device['identified'] = True

        # Bookeen
        if 'bookeen/cybook' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Bookeen'
            self.device['model'] = 'Cybook'
            self.device['type'] = 'ereader'

            if 'Orizon' in self.ua:
                self.device['model'] = 'Cybook Orizon'

            self.device['identified'] = True

        # Sony Reader
        if 'EBRD1101' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Sony'
            self.device['model'] = 'Reader'
            self.device['type'] = 'ereader'
            self.device['identified'] = True

        # iRiver
        if 'Iriver' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'iRiver'
            self.device['model'] = 'Story'
            self.device['type'] = 'ereader'
            if 'EB07' in self.ua:
                self.device['model'] = 'Story HD EB07'
            self.device['identified'] = True

        # Nintendo
        #   Opera/9.30 (Nintendo Wii; U; ; 3642; en)
        #   Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)
        #   Opera/9.50 (Nintendo DSi; Opera/507; U; en-US)
        #   Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7455.US
        #   Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7455.EU
        if 'Nintendo Wii' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Nintendo'
            self.device['model'] = 'Wii'
            self.device['type'] = 'gaming'
            self.device['identified'] = True

        if 'Nintendo DSi' in self.ua:
            self.os.name = ''
            self.device['manufacturer'] = 'Nintendo'
            self.device['model'] = 'DSi'
            self.device['type'] = 'gaming'
            self.device['identified'] = True

        if 'Nintendo 3DS' in self.ua:
            self.os.name = ''
            self.device['manufacturer'] = 'Nintendo'
            self.device['model'] = '3DS'
            self.device['type'] = 'gaming'

            match = re.search(r'Version/([0-9.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)
            self.device['identified'] = True

        # Sony PlayStation
        if 'PlayStation Portable' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Sony'
            self.device['model'] = 'PlayStation Portable'
            self.device['type'] = 'gaming'
            self.device['identified'] = True

        if 'PlayStation Vita' in self.ua:
            self.os['name'] = ''
            
            match = re.search(r'PlayStation Vita ([0-9.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)

            self.device['manufacturer'] = 'Sony'
            self.device['model'] = 'PlayStation Vita'
            self.device['type'] = 'gaming'
            self.device['identified'] = True

        if 'PlayStation 3'.lower() in self.ua.lower():
            self.os['name'] = ''
            match = re.search(r'PLAYSTATION 3;? ([0-9.]*)', self.ua)
            if match:
                self.os['version']['value'] = match.group(1)
            self.device['manufacturer'] = 'Sony'
            self.device['model'] = 'PlayStation 3'
            self.device['type'] = 'gaming'
            self.device['identified'] = True

        # Panasonic Smart Viera
        #   Mozilla/5.0 (FreeBSD; U; Viera; ja-JP) AppleWebKit/535.1 (KHTML, like Gecko) Viera/1.2.4 Chrome/14.0.835.202 Safari/535.1
        if 'Viera' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Panasonic'
            self.device['model'] = 'Smart Viera'
            self.device['type'] = 'television'
            self.device['identified'] = True

        # Sharp AQUOS TV
        #   Mozilla/5.0 (DTV) AppleWebKit/531.2  (KHTML, like Gecko) AQUOSBrowser/1.0 (US00DTV;V;0001;0001)
        #   Mozilla/5.0 (DTV) AppleWebKit/531.2+ (KHTML, like Gecko) Espial/6.0.4 AQUOSBrowser/1.0 (CH00DTV;V;0001;0001)
        #   Opera/9.80 (Linux armv6l; U; en) Presto/2.8.115 Version/11.10 AQUOS-AS/1.0 LC-40LE835X
        if 'AQUOSBrowser' in self.ua or 'AQUOS-AS' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = STRINGS_SHARP
            self.device['model'] = 'Aquos TV'
            self.device['type'] = 'television'
            self.device['identified'] = True
        # Samsung Smart TV
        #
        #   Mozilla/5.0 (SmartHub; SMART-TV; U; Linux/SmartTV; Maple2012) AppleWebKit/534.7 (KHTML, like Gecko) SmartTV Safari/534.7
        #   Mozilla/5.0 (SmartHub; SMART-TV; U; Linux/SmartTV) AppleWebKit/531.2+ (KHTML, like Gecko) WebBrowser/1.0 SmartTV Safari/531.2+
        if 'SMART-TV' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = STRINGS_SAMSUNG
            self.device['model'] = 'Smart TV'
            self.device['type'] = 'television'
            self.device['identified'] = True

            match = re.search(r'Maple([0-9]*)', self.ua)
            if match:
                self.device['model'] += ' ' + match.group(1)

        # Sony Internet TV
        #
        #   Opera/9.80 (Linux armv7l; U; InettvBrowser/2.2(00014A;SonyDTV115;0002;0100) KDL-46EX640; CC/USA; en) Presto/2.8.115 Version/11.10
        #   Opera/9.80 (Linux armv7l; U; InettvBrowser/2.2(00014A;SonyDTV115;0002;0100) KDL-40EX640; CC/USA; en) Presto/2.10.250 Version/11.60
        #   Opera/9.80 (Linux armv7l; U; InettvBrowser/2.2(00014A;SonyDTV115;0002;0100) N/A; CC/USA; en) Presto/2.8.115 Version/11.10
        #   Opera/9.80 (Linux mips; U; InettvBrowser/2.2 (00014A;SonyDTV115;0002;0100) ; CC/JPN; en) Presto/2.9.167 Version/11.50
        #   Opera/9.80 (Linux mips; U; InettvBrowser/2.2 (00014A;SonyDTV115;0002;0100) AZ2CVT2; CC/CAN; en) Presto/2.7.61 Version/11.00
        #   Opera/9.80 (Linux armv6l; Opera TV Store/4207; U; (SonyBDP/BDV11); en) Presto/2.9.167 Version/11.50
        #   Opera/9.80 (Linux armv6l ; U; (SonyBDP/BDV11); en) Presto/2.6.33 Version/10.60
        #   Opera/9.80 (Linux armv6l; U; (SonyBDP/BDV11); en) Presto/2.8.115 Version/11.10
        if re.search(r'SonyDTV|SonyBDP|SonyCEBrowser', self.ua):
            self.os['name'] = ''
            self.device['manufacturer'] = 'Sony'
            self.device['model'] = 'Internet TV'
            self.device['type'] = 'television'
            self.device['identified'] = True

        # Philips Net TV
        #
        #   Opera/9.70 (Linux armv6l ; U; CE-HTML/1.0 NETTV/2.0.2; en) Presto/2.2.1
        #   Opera/9.80 (Linux armv6l ; U; CE-HTML/1.0 NETTV/3.0.1;; en) Presto/2.6.33 Version/10.60
        #   Opera/9.80 (Linux mips; U; CE-HTML/1.0 NETTV/3.0.1; PHILIPS-AVM-2012; en) Presto/2.9.167 Version/11.50
        #   Opera/9.80 (Linux mips ; U; HbbTV/1.1.1 (; Philips; ; ; ; ) CE-HTML/1.0 NETTV/3.1.0; en) Presto/2.6.33 Version/10.70
        #   Opera/9.80 (Linux i686; U; HbbTV/1.1.1 (; Philips; ; ; ; ) CE-HTML/1.0 NETTV/3.1.0; en) Presto/2.9.167 Version/11.50
        if 'NETTV/' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Philips'
            self.device['model'] = 'Net TV'
            self.device['type'] = 'television'
            self.device['identified'] = True
        #LG NetCast TV
        #
        #   Mozilla/5.0 (DirectFB; Linux armv7l) AppleWebKit/534.26+ (KHTML, like Gecko) Version/5.0 Safari/534.26+ LG Browser/5.00.00(+mouse+3D+SCREEN+TUNER; LGE; GLOBAL-PLAT4; 03.09.22; 0x00000001;); LG NetCast.TV-2012
        #   Mozilla/5.0 (DirectFB; Linux armv7l) AppleWebKit/534.26+ (KHTML, like Gecko) Version/5.0 Safari/534.26+ LG Browser/5.00.00(+SCREEN+TUNER; LGE; GLOBAL-PLAT4; 01.00.00; 0x00000001;); LG NetCast.TV-2012
        #   Mozilla/5.0 (DirectFB; U; Linux armv6l; en) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  LG Browser/4.1.4( BDP; LGE; Media/BD660; 6970; abc;); LG NetCast.Media-2011
        #   Mozilla/5.0 (DirectFB; U; Linux 7631; en) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  LG Browser/4.1.4( NO_NUM; LGE; Media/SP520; ST.3.97.409.F; 0x00000001;); LG NetCast.Media-2011
        #   Mozilla/5.0 (DirectFB; U; Linux 7630; en) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  LG Browser/4.1.4( 3D BDP NO_NUM; LGE; Media/ST600; LG NetCast.Media-2011
        #   (LGSmartTV/1.0) AppleWebKit/534.23 OBIGO-T10/2.0
        if re.search(r'LG NetCast\.(?:TV|Media)-([0-9]*)', self.ua):
            match = re.search(r'LG NetCast\.(?:TV|Media)-([0-9]*)', self.ua)
            self.os['name'] = ''
            self.device['manufacturer'] = STRINGS_LG
            self.device['model'] = 'NetCast TV ' + match.group(1)
            self.device['type'] = 'television'
            self.device['identified'] = True

        if 'LGSmartTV' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = STRINGS_LG
            self.device['model'] = 'Smart TV'
            self.device['type'] = 'television'
            self.device['identified'] = True

        # Toshiba Smart TV
        #
        #   Mozilla/5.0 (Linux mipsel; U; HbbTV/1.1.1 (; TOSHIBA; DTV_RL953; 56.7.66.7; t12; ) ; ToshibaTP/1.3.0 (+VIDEO_MP4+VIDEO_X_MS_ASF+AUDIO_MPEG+AUDIO_MP4+DRM+NATIVELAUNCH) ; en) AppleWebKit/534.1 (KHTML, like Gecko)
        #   Mozilla/5.0 (DTV; TSBNetTV/T32013713.0203.7DD; TVwithVideoPlayer; like Gecko) NetFront/4.1 DTVNetBrowser/2.2 (000039;T32013713;0203;7DD) InettvBrowser/2.2 (000039;T32013713;0203;7DD)
        #   Mozilla/5.0 (Linux mipsel; U; HbbTV/1.1.1 (; TOSHIBA; 40PX200; 0.7.3.0.; t12; ) ; Toshiba_TP/1.3.0 (+VIDEO_MP4+AUDIO_MPEG+AUDIO_MP4+VIDEO_X_MS_ASF+OFFLINEAPP) ; en) AppleWebKit/534.1 (KHTML, like Gec
        if re.search(r'Toshiba_?TP/', self.ua) or re.search(r'TSBNetTV/', self.ua):
            self.os['name'] = ''
            self.device['manufacturer'] = 'Toshiba'
            self.device['model'] = 'Smart TV'
            self.device['type'] = 'television'
            self.device['identified'] = True

        # MachBlue XT
        if re.search(r'mbxtWebKit/([0-9.]*)', self.ua):
            match = re.search(r'mbxtWebKit/([0-9.]*)', self.ua)
            self.os.name = ''
            self.browser.name = 'MachBlue XT'
            self.browser['version']['value'] = match.group(1)
            self.browser['version']['details'] = 2
            self.device['type'] = 'television'

        # ADB
        if re.search(r'\(ADB; ([^\)]+)\)', self.ua):
            match = re.search(r'\(ADB; ([^\)]+)\)', self.ua)
            self.os['name'] = ''
            self.device['manufacturer'] = 'ADB'
            self.device['model'] = (match.group(1).replace('ADB', '') if match.group(1) != 'Unknown' else '') + 'IPTV receiver'
            self.device['type'] = 'television'
            self.device['identified'] = True

        # MStar
        if 'Master;OWB' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'MStar'
            self.device['model'] = 'PVR'
            self.device['type'] = 'television'
            self.device['identified'] = True
            self.browser.name = 'Origyn Web Browser'

        # TechniSat
        if re.search('\\TechniSat ([^;]+);', self.ua):
            match = re.search(r'\\TechniSat ([^;]+);', self.ua)
            self.os['name'] = ''
            self.device['manufacturer'] = 'TechniSat'
            self.device['model'] = match.group(1)
            self.device['type'] = 'television'
            self.device['identified'] = True

        # Technicolor
        if re.search('\\Technicolor_([^;]+);', self.ua):
            match = re.search('\\Technicolor_([^;]+);', self.ua)
            self.os['name'] = ''
            self.device['manufacturer'] = 'Technicolor'
            self.device['model'] = match.group(1)
            self.device['type'] = 'television'
            self.device['identified'] = True

        # Winbox Evo2
        if 'Winbox Evo2' in self.ua:
            self.os['name'] = ''
            self.device['manufacturer'] = 'Winbox'
            self.device['model'] = 'Evo2'
            self.device['type'] = 'television'
            self.device['identified'] = True

        # Roku
        if re.search(r'^Roku/DVP-([0-9]+)', self.ua):
            self.device['manufacturer'] = 'Roku'
            self.device['type'] = 'television'
            match = re.search(r'^Roku/DVP-([0-9]+)', self.ua).group(1)
            if match == '2000':
                self.device['model'] = 'HD'
            elif match == '2050':
                self.device['model'] = 'XD'
            elif match == '2100':
                self.device['model'] = 'XDS'
            elif match == '2400':
                self.device['model'] = 'LT'
            elif match == '3000':
                self.device['model'] = '2 HD'
            elif match == '3050':
                self.device['model'] = '2 XD'
            elif match == '3100':
                self.device['model'] = '2 XS'

            self.device['identified'] = True

        if re.search(r'HbbTV/1.1.1 \([^;]*;\s*([^;]*)\s*;\s*([^;]*)\s*;', self.ua):
            match = re.search(r'HbbTV/1.1.1 \([^;]*;\s*([^;]*)\s*;\s*([^;]*)\s*;', self.ua)
            vendorName = match.group(1).strip()
            modelName = match.group(2).strip()
            if not self.device.get('manufacturer', False) and vendorName != '' and vendorName != 'vendorName':
                if vendorName == 'LGE':
                    self.device['manufacturer'] = 'LG'
                elif vendorName == 'TOSHIBA':
                    self.device['manufacturer'] = 'Toshiba'
                elif vendorName == 'smart':
                    self.device['manufacturer'] = 'Smart'
                elif vendorName == 'tv2n':
                    self.device['manufacturer'] = 'TV2N'
                else:
                    self.device['manufacturer'] = vendorName

                if not self.device.get('model', False) and modelName != '' and modelName != 'modelName':
                    if modelName == 'GLOBAL_PLAT3':
                        self.device['model'] = 'NetCast TV'
                    elif modelName == 'SmartTV2012':
                        self.device['model'] = 'Smart TV 2012'
                    elif modelName == 'videoweb':
                        self.device['model'] = 'Videoweb'
                    else:
                        self.device['model'] = modelName

                    if vendorName == 'Humax':
                        self.device['model'] = self.device['model'].upper()

                    self.device['identified'] = True
                    self.os['name'] = ''
            self.device['type'] = 'television';
        
        # Detect type based on common identifiers
        if 'InettvBrowser' in self.ua:
            self.device['type'] = 'television'
        if 'MIDP' in self.ua:
            self.device['type'] = 'mobile'

        # Try to detect any devices based on common locations of model ids
        if not self.device.get('model', False) and not self.device.get('manufacturer', False):
            candidates = []
            if not re.search(r'^(Mozilla|Opera)', self.ua):
                match = re.search(r'^(?:MQQBrowser/[0-9\.]+/)?([^\s]+)', self.ua)
                group = match.group(1)
                if match:
                    group = re.sub(r'_TD$', '', group)
                    group = re.sub(r'_CMCC$', '', group)
                    group = re.sub(r'[_ ]Mozilla$', '', group)
                    group = re.sub(r' Linux$', '', group)
                    group = re.sub(r' Opera$', '', group)
                    group = re.sub(r'/[0-9].*$', '', group)

                    candidates.append(group)
            if re.search(r'[0-9]+x[0-9]+; ([^;]+)', self.ua):
                candidates.append(re.search(r'[0-9]+x[0-9]+; ([^;]+)', self.ua).group(1))
            
            if re.search(r'[0-9]+X[0-9]+ ([^;/\(\)]+)', self.ua):
                candidates.append(re.search(r'[0-9]+X[0-9]+ ([^;/\(\)]+)', self.ua).group(1))
            
            if re.search(r'Windows NT 5.1; ([^;]+); Windows Phone', self.ua):
                candidates.append(re.search(r'Windows NT 5.1; ([^;]+); Windows Phone', self.ua).group(1))

            if re.search(r'\) PPC; (?:[0-9]+x[0-9]+; )?([^;/\(\)]+)', self.ua):
                candidates.append(re.search(r'\) PPC; (?:[0-9]+x[0-9]+; )?([^;/\(\)]+)', self.ua).group(1))

            if re.search(r'\(([^;]+); U; Windows Mobile', self.ua):
                candidates.append(re.search(r'\(([^;]+); U; Windows Mobile', self.ua).group(1))

            if re.search(r'Vodafone/1.0/([^/]+)', self.ua):
                candidates.append(re.search(r'Vodafone/1.0/([^/]+)', self.ua).group(1))

            if re.search('\\ ([^\s]+)$', self.ua):
                candidates.append(re.search('\\ ([^\s]+)$', self.ua).group(1))

            for candidate in candidates:
                if not self.device.get('model', False) and not self.device.get('manufacturer', False):
                    model = self.cleanup_model(candidate)
                    result = False

                    if self.os.get('name', '') == 'Android':
                        if model in ANDROID_MODELS:
                            self.device['manufacturer'] = ANDROID_MODELS[model][0]
                            self.device['model'] = ANDROID_MODELS[model][1]
                            if len(ANDROID_MODELS[model]) > 2:
                                self.device['type'] = ANDROID_MODELS[model][2]
                            self.device['identified'] = True
                            result = True
                    
                    if not self.os.get('name', False) or self.os['name'] in ['Windows', 'Windows Mobile', 'Windows CE']:
                        if model in WINDOWS_MOBILE_MODELS:
                            self.device['manufacturer'] = WINDOWS_MOBILE_MODELS[model][0]
                            self.device['model'] = WINDOWS_MOBILE_MODELS[model][1]
                            self.device['type'] = 'mobile'
                            self.device['identified'] = True

                            if self.os['name'] != 'Windows Mobile':
                                self.os['name'] = 'Windows Mobile'
                                self.os['version']['value'] = None

                            result = True
                if not result:
                    if re.search(r'^GIONEE-([^\s]+)', candidate):
                        match = re.search(r'^GIONEE-([^\s]+)', candidate)
                        self.device['manufacturer'] = 'Gionee'
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True

                    if re.search(r'^HTC_?([^/_]+)(?:/|_|$)', candidate):
                        match = re.search(r'^HTC_?([^/_]+)(?:/|_|$)', candidate)
                        self.device['manufacturer'] = STRINGS_HTC
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True
                    
                    if re.search(r'^HUAWEI-([^/]*)', candidate):
                        match = re.search(r'^HUAWEI-([^/]*)', candidate)
                        self.device['manufacturer'] = STRINGS_HUAWEI
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True
                    
                    if re.search(r'(?:^|\()LGE?(?:/|-|_|\s)([^\s]*)', candidate):
                        match = re.search(r'(?:^|\()LGE?(?:/|-|_|\s)([^\s]*)', candidate)
                        self.device['manufacturer'] = STRINGS_LG
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True

                    if re.search(r'^MOT-([^/_]+)(?:/|_|$)', candidate):
                        match = re.search(r'^MOT-([^/_]+)(?:/|_|$)', candidate)
                        self.device['manufacturer'] = STRINGS_MOTOROLA
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True

                    if re.search(r'^Motorola_([^/_]+)(?:/|_|$)', candidate):
                        match = re.search(r'^Motorola_([^/_]+)(?:/|_|$)', candidate)
                        self.device['manufacturer'] = STRINGS_MOTOROLA
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True

                    if re.search(r'^Nokia([^/]+)(?:/|$)', candidate):
                        match = re.search(r'^Nokia([^/]+)(?:/|$)', candidate)
                        self.device['manufacturer'] = 'Nokia'
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True

                        if not self.os['name']:
                            self.os['name'] = 'Series40'
                    
                    if re.search(r'^SonyEricsson([^/_]+)(?:/|_|$)', candidate):
                        match = re.search(r'^SonyEricsson([^/_]+)(?:/|_|$)', candidate)
                        self.device['manufacturer'] = STRINGS_SONY_ERICSSON
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'
                        self.device['identified'] = True

                    if re.search(r'^SAMSUNG-([^/_]+)(?:/|_|$)', candidate):
                        match = re.search(r'^SAMSUNG-([^/_]+)(?:/|_|$)', candidate)
                        self.device['manufacturer'] = STRINGS_SAMSUNG
                        self.device['model'] = self.cleanup_model(match.group(1))
                        self.device['type'] = 'mobile'

                        if self.os['name'] == 'Bada':
                            manufacturer = 'SAMSUNG'
                            model = self.cleanup_model(self.device['model'])

                            if manufacturer in BADA_MODELS and model in BADA_MODELS[manufacturer]:
                                self.device['manufacturer'] = BADA_MODELS[manufacturer][model][0]
                                self.device['model'] = BADA_MODELS[manufacturer][model][1]
                                self.device['identified'] = True
                        elif re.search(r'Jasmine/([0-9.]*', self.ua):
                            match = re.search(r'Jasmine/([0-9.]*', self.ua)
                            version = match.group(1)
                            manufacturer = 'SAMSUNG'
                            model = self.cleanup_model(self.device['model'])

                            if manufacturer in TOUCHWIZ_MODELS and model in TOUCHWIZ_MODELS[manufacturer]:
                                self.device['manufacturer'] = TOUCHWIZ_MODELS[manufacturer][model][0]
                                self.device['model'] = TOUCHWIZ_MODELS[manufacturer][model][1]
                                self.device['identified'] = True
                                self.os['name'] = 'Touchwiz'
                                self.os['version']['value'] = '2.0'
                        elif re.search(r'Dolfin/([0-9.]*)', self.ua):
                            match = re.search(r'Dolfin/([0-9.]*)', self.ua)
                            version = match.group(1)
                            manufacturer = 'SAMSUNG'
                            model = self.cleanup_model(self.device['model'])
                            if manufacturer in BADA_MODELS and model in BADA_MODELS[manufacturer]:
                                self.device['manufacturer'] = BADA_MODELS[manufacturer][model][0]
                                self.device['model'] = BADA_MODELS[manufacturer][model][1]
                                self.device['identified'] = True
                                self.os['name'] = 'Bada'
                                if version == '2.0':
                                    self.os['version']['value'] = '1.0'
                                elif version == '2.2':
                                    self.os['version']['value'] = '1.2'
                                elif version == '3.0':
                                    self.os['version']['value'] = '2.0'
                            
                            if manufacturer in TOUCHWIZ_MODELS and model in TOUCHWIZ_MODELS[manufacturer]:
                                self.device['manufacturer'] = TOUCHWIZ_MODELS[manufacturer][model][0]
                                self.device['model'] = TOUCHWIZ_MODELS[manufacturer][model][1]
                                self.device['identified'] = True
                                self.os['name'] = 'Touchwiz'

                                if version == '1.0':
                                    self.os['version']['value'] = '1.0'
                                elif version == '1.5':
                                    self.os['version']['value'] = '2.0'
                                elif version == '2.0':
                                    self.os['version']['value'] = '3.0'

        if re.search(r'\((?:LG[-|/])(.*) (?:Browser/)?AppleWebkit', self.ua):
            match = re.search(r'\((?:LG[-|/])(.*) (?:Browser/)?AppleWebkit', self.ua)
            self.device['manufacturer'] = STRINGS_LG
            self.device['model'] = match.group(1)
            self.device['type'] = 'mobile'
            self.device['identified'] = True

        if re.search(r'^Mozilla/5.0 \((?:Nokia|NOKIA)(?:\s?)([^\)]+)\)UC AppleWebkit\(like Gecko\) Safari/530$', self.ua):
            match = re.search(r'^Mozilla/5.0 \((?:Nokia|NOKIA)(?:\s?)([^\)]+)\)UC AppleWebkit\(like Gecko\) Safari/530$', self.ua)
            self.device['manufacturer'] = 'Nokia'
            self.device['model'] = match.group(1)
            self.device['type'] = 'mobile'
            self.device['identified'] = True
            self.os['name'] = 'Series60'

    def _parse_browser(self):
        # Safari
        if 'Safari' in self.ua:
            if self.os['name'] == 'iOS':
                self.browser['stock'] = True
                self.browser['hidden'] = True
                self.browser['name'] = 'Safari'
                self.browser['version']['value'] = None

            if self.os['name'] == 'Mac OS X' or self.os['name'] == 'Windows':
                self.browser['name'] = 'Safari'
                self.browser['stock'] = (self.os['name'] == 'Mac OS X')

                if re.search(r'Version/([0-9\.]+)', self.ua):
                    self.browser['version']['value'] = re.search(r'Version/([0-9\.]+)', self.ua).group(1)
                if re.search(r'AppleWebKit/[0-9\.]+\+', self.ua):
                    self.browser['name'] = 'WebKit Nightly Build'
                    self.browser['version']['value'] = None

        # Internet Explorer
        if 'MSIE' in self.ua:
            self.browser['name'] = 'Internet Explorer'
            if 'IEMobile' in self.ua or 'Windows CE' in self.ua or 'Windows Phone' in self.ua or 'WP7' in self.ua:
                self.browser['name'] = 'Mobile Internet Explorer'
            if re.search(r'MSIE ([0-9.]*)', self.ua):
                self.browser['version']['value'] = re.search(r'MSIE ([0-9.]*)', self.ua).group(1)

        # Opera
        if 'opera' in self.ua.lower():
            self.browser['stock'] = False
            self.browser['name'] = 'Opera'

            if re.search(r'Opera[/| ]([0-9.]*)', self.ua):
                self.browser['version']['value'] = re.search(r'Opera[/| ]([0-9.]*)', self.ua).group(1)
            if re.search(r'Version/([0-9.]*)', self.ua):
                match = re.search(r'Version/([0-9.]*)', self.ua)
                if float(match.group(1)) >= 10:
                    self.browser['version']['value'] = match.group(1)
                else:
                    self.browser['version']['value'] = None

            if self.browser.get('version', False) and 'Edition Labs' in self.ua:
                self.browser['version']['type'] = 'alpha'
                self.browser['channel'] = 'Labs'

            if self.browser.get('version', False) and 'Edition Next' in self.ua:
                self.browser['version']['type'] = 'alpha'
                self.browser['channel'] = 'Next'

            if 'Opera Tablet' in self.ua:
                self.browser['name'] = 'Opera Mobile'
                self.device['type'] = 'tablet'

            if 'Opera Mobi' in self.ua:
                self.browser['name'] = 'Opera Mobile'
                self.device['type'] = 'mobile'

            if 'Opera Mini;' in self.ua:
                self.browser['name'] = 'Opera Mini'
                self.browser['version']['value'] = None
                self.browser['mode'] = 'proxy'
                self.device['type'] = 'mobile'

            if re.search(r'Opera Mini/(?:att/)?([0-9.]*)', self.ua):
                match = re.search(r'Opera Mini/(?:att/)?([0-9.]*)', self.ua)
                self.browser['name'] = 'Opera Mini'
                self.browser['version']['value'] = match.group(1)
                self.browser['version']['details'] = -1
                self.browser['mode'] = 'proxy'
                self.device['type'] = 'mobile'

            if self.browser['name'] == 'Opera' and self.device['type'] == 'mobile':
                self.browser['name'] = 'Opera Mobile'
                if 'BER' in self.ua:
                    self.browser['name'] = 'Opera Mini'
                    self.browser['version']['value'] = None

            if 'InettvBrowser' in self.ua:
                self.device['type'] = 'television'

            if 'Opera TV' in self.ua or 'Opera-TV' in self.ua:
                self.browser['name'] = 'Opera'
                self.device['type'] = 'television'

            if 'Linux zbov' in self.ua:
                self.browser['name'] = 'Opera Mobile'
                self.browser['mode'] = 'desktop'
                self.device['type'] = 'mobile'
                self.os['name'] = None
                self.os['version']['value'] = None

            if 'Linux zvav' in self.ua:
                self.browser['name'] = 'Opera Mini'
                self.browser['version']['value'] = None
                self.browser['mode'] = 'desktop'
                self.device['type'] = 'mobile'
                self.os['name'] = None
                self.os['version']['value'] = None

        # Firefox
        if 'Firefox' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Firefox'

            if re.search(r'Firefox/([0-9ab.]*)', self.ua):
                self.browser['version']['value'] = re.search(r'Firefox/([0-9ab.]*)', self.ua).group(1)

            if self.browser['version'].get('type', '') == 'alpha':
                self.browser['channel'] = 'Aurora'

            if self.browser['version'].get('type', '') == 'beta':
                self.browser['channel'] = 'Beta'

            if 'Fennec' in self.ua:
                self.device['type'] = 'mobile'

            if 'Mobile; rv' in self.ua:
                self.device['type'] = 'mobile'

            if 'Tablet; rv' in self.ua:
                self.device['type'] = 'tablet'

            if self.device.get('type', False) == 'mobile' or self.device.get('type', False) == 'tablet':
                self.browser['name'] = 'Firefox Mobile'

        if 'Namoroka' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Firefox'

            if re.search(r'/Namoroka/([0-9ab.]*)', self.ua):
                self.browser['version']['value'] = re.search(r'/Namoroka/([0-9ab.]*)', self.ua).group(1)

            self.browser['channel'] = 'Namoroka'

        if 'Shiretoko' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Firefox'

            match = re.search(r'Shiretoko/([0-9ab.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

            self.browser['channel'] = 'Shiretoko'

        if 'Minefield' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Firefox'

            match = re.search(r'Minefield/([0-9ab.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

            self.browser['channel'] = 'Minefield'

        if 'Firebird' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Firebird'

            match = re.search(r'Firebird/([0-9ab.]*', self.ua)
            self.browser['version']['value'] = match.group(1)

        # SeaMonkey
        if 'SeaMonkey' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'SeaMonkey'

            match = re.search(r'SeaMonkey/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Netscape
        if 'Netscape' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Netscape'
            match = re.search(r'Netscape[0-9]?/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Konqueror
        if 'konqueror' in self.ua.lower():
            self.browser['name'] = 'Konqueror'
            match = re.search(r'[k|K]onqueror/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Chrome
        if re.search(r'(?:Chrome|CrMo|CriOS)/([0-9.]*)', self.ua):
            match = re.search(r'(?:Chrome|CrMo|CriOS)/([0-9.]*)', self.ua)
            self.browser['stock'] = False
            self.browser['name'] = 'Chrome'
            self.browser['version']['value'] = match.group(1)

            version_prefix = '.'.join(match.group(1).split('.')[0:3])
            if self.os['name'] == 'Android':
                if version_prefix == '16.0.912':
                    self.browser['channel'] = 'Beta'
                elif version_prefix == '18.0.1025':
                    self.browser['version']['details'] = 1
                else:
                    self.browser['channel'] = 'Nightly'
            else:
                if version_prefix in ['0.2.149', '0.3.154', '0.4.154', '1.0.154', '2.0.172', '3.0.195', '4.0.249', '4.1.249', '5.0.375', '6.0.472', '7.0.517', '8.0.552', '9.0.597', '10.0.648', '11.0.696', '12.0.742', '13.0.782', '14.0.835', '15.0.874', '16.0.912', '17.0.963', '18.0.1025', '19.0.1084', '20.0.1132', '21.0.1180']:
                    if self.browser['version'].get('minor', None) == 0:
                        self.browser['version']['details'] = 1
                    else:
                        self.browser['version']['details'] = 2
                else:
                    self.browser['channel'] = 'Nightly'

        # Chrome Frame
        if 'chromeframe' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'Chrome Frame'

            match = re.search(r'chromeframe/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Chromium
        if 'Chromium' in self.ua:
            self.browser['stock'] = False
            self.browser['channel'] = ''
            self.browser['name'] = 'Chromium'

            match = re.search(r'Chromium/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # BrowserNG
        if 'BrowserNG' in self.ua:
            self.browser['name'] = 'Nokia Browser'
            match = re.search(r'BrowserNG/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)
                self.browser['version']['details'] = 3
                self.browser['version']['builds'] = False

        # Nokia Browser
        if 'NokiaBrowser' in self.ua:
            self.browser['name'] = 'Nokia Browser'
            match = re.search(r'NokiaBrowser/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)
                self.browser['version']['details'] = 3

        # MicroB
        if re.search(r'Maemo[ |_]Browser', self.ua):
            self.browser['name'] = 'MicroB'
            match = re.search(r'Maemo[ |_]Browser[ |_]([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)
                self.browser['version']['details'] = 3

        # NetFront
        if 'NetFront' in self.ua:
            self.browser['name'] = 'NetFront'
            self.device['type'] = 'mobile'
            match = re.search(r'NetFront/([0-9.]*)', self.ua)
            self.browser['version']['value'] = match.group(1)
            if 'InettvBrowser' in self.ua:
                self.device['type'] = 'television'

        # Silk
        if 'Silk' in self.ua:
            if 'Silk-Accelerated'in self.ua:
                self.browser['name'] = 'Silk'

                match = re.search(r'Silk/([0-9.]*)', self.ua)
                if match:
                    self.browser['version']['value'] = match.group(1)
                    self.browser['version']['details'] = 2
                self.device['manufacturer'] = 'Amazon'
                self.device['model'] = 'Kindle Fire'
                self.device['type'] = 'tablet'
                self.device['identified'] = True

                if 'name' not in self.os or self.os['name'] != 'Android':
                    self.os['name'] = 'Android'
                    self.os['version']['value'] = None

        # Dolfin
        if 'Dolfin' in self.ua:
            self.browser['name'] = 'Dolfin'
            match = re.search(r'Dolfin/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Iris
        if 'Iris' in self.ua:
            self.browser['name'] = 'Iris'
            self.device['type'] = 'mobile'
            self.device['model'] = None
            self.device['manufacturer'] = None
            self.os['name'] = 'Windows Mobile'
            self.os['version']['value'] = None

            match = re.search(r'Iris/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

            match = re.search(r' WM([0-9]) ', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1) + '.0'
            else:
                self.browser['mode'] = 'desktop'

        #Jasmine
        if 'Jasmine' in self.ua:
            self.browser['name'] = 'Jasmine'
            match = re.search(r'Jasmine/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Boxee
        if 'Boxee' in self.ua:
            self.browser['name'] = 'Boxee'
            self.device['type'] = 'television'

            match = re.search(r'Boxee/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # Espial
        if 'Espial' in self.ua:
            self.browser['name'] = 'Espial'
            self.os['name'] = ''
            self.os['version']['value'] = None

            if self.device.get('type', None) != 'television':
                self.device['type'] = 'television'
                self.device['model'] = None
                self.device['manufacturer'] = None

            match = re.search(r'Espial/([0-9.]*)', self.ua)
            if match:
                self.browser['version']['value'] = match.group(1)

        # ANT Galio
        if re.search(r'ANTGalio/([0-9.]*)', self.ua):
            match = re.search(r'ANTGalio/([0-9.]*)', self.ua)
            self.browser['name'] = 'ANT Galio'
            self.browser['version']['value'] = match.group(1)
            self.browser['version']['details'] = 3
            self.device['type'] = 'television'

        # NetFront NX
        if re.search(r'NX/([0-9.]*)', self.ua):
            match = re.search(r'NX/([0-9.]*)', self.ua)
            self.browser['name'] = 'NetFront NX'
            self.browser['version']['value'] = match.group(1)
            self.browser['version']['details'] = 2
            if 'DTV' in self.ua.upper():
                self.device['type'] = 'television'
            elif 'mobile' in self.ua.lower():
                self.device['type'] = 'mobile'
            else:
                self.device['type'] = 'desktop'
            self.os['name'] = None
            self.os['version']['value'] = None

        # Obigo
        if 'obigo' in self.ua.lower():
            self.browser['name'] = 'Obigo'

            if re.search(r'Obigo/([0-9.]*)', self.ua, re.I):
                self.browser['version']['value'] = re.search(r'Obigo/([0-9.]*)', self.ua, re.I).group(1)

            if re.search(r'Obigo/([A-Z])([0-9.]*)', self.ua, re.I):
                match = re.search(r'Obigo/([A-Z])([0-9.]*)', self.ua, re.I)
                self.browser['name'] = 'Obigo ' + match.group(1)
                self.browser['version']['value'] = re.search(r'Obigo/([0-9.]*)', self.ua, re.I).group(2)

            if re.search(r'Obigo-([A-Z])([0-9.]*)/', self.ua, re.I):
                match = re.search(r'Obigo-([A-Z])([0-9.]*)/', self.ua, re.I)
                self.browser['name'] = 'Obigo ' + match.group(1)
                self.browser['version']['value'] = re.search(r'Obigo/([0-9.]*)', self.ua, re.I).group(2)

        # UC Web
        if 'UCWEB' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = 'UC Browser'

            if re.search(r'UCWEB([0-9]*[.][0-9]*)', self.ua):
                self.browser['version']['value'] = re.search(r'UCWEB([0-9]*[.][0-9]*)', self.ua).group(1)
                self.browser['version']['details'] = 3

            if self.os['name'] == 'Linux':
                self.os['name'] = ''

            self.device['type'] = 'mobile'

            if re.search(r'^IUC \(U;\s?iOS ([0-9\.]+);', self.ua):
                self.os['name'] = 'iOS'
                self.os['version']['value'] = re.search(r'^IUC \(U;\s?iOS ([0-9\.]+);', self.ua).group(1)

            if re.search(r'^JUC \(Linux; U; ([0-9\.]+)[^;]*; [^;]+; ([^;]*[^\s])\s*; [0-9]+\*[0-9]+\)', self.ua):
                match = re.search(r'^JUC \(Linux; U; ([0-9\.]+)[^;]*; [^;]+; ([^;]*[^\s])\s*; [0-9]+\*[0-9]+\)', self.ua)
                model = self.cleanup_model(match.group(2))

                self.os['name'] = 'Android'
                self.os['version']['value'] = match.group(1)

                if model in ANDROID_MODELS:
                    self.device['manufacturer'] = ANDROID_MODELS[model][0]
                    self.device['model'] = ANDROID_MODELS[model][1]
                    if len(ANDROID_MODELS[model]) > 2:
                        self.device['type'] = ANDROID_MODELS[model][2]
                    self.device['identified'] = True

            if re.search(r'\) UC', self.ua):
                self.browser['stock'] = False
                self.browser['name'] = 'UC Browser'

            if re.search(r'UCBrowser/([0-9.]*)', self.ua):
                self.browser['stock'] = False
                self.browser['name'] = 'UC Browser'
                self.browser['version']['value'] = re.search(r'UCBrowser/([0-9.]*)', self.ua).group(1)
                self.browser['version']['details'] = 2

        # NineSky
        if re.search(r'NineSky(?:-android-mobile(?:-cn)?)?/([0-9.]*)', self.ua):
            self.browser['name'] = 'NineSky'
            self.browser['version']['value'] = re.search(r'NineSky(?:-android-mobile(?:-cn)?)?/([0-9.]*)', self.ua).group(1)
            
            if self.os.get('name', None) != 'Android':
                self.os['name'] = 'Android'
                self.os['version']['value'] = None

                self.device['manufacturer'] = None
                self.device['model'] = None

        # Skyfire
        if re.search(r'Skyfire/([0-9.]*)', self.ua):
            self.browser['name'] = 'Skyfire'
            self.browser['version']['value'] = re.search(r'Skyfire/([0-9.]*)', self.ua).group(1)
            self.device['type'] = 'mobile'
            self.os['name'] = 'Android'
            self.os['version']['value'] = None

        # Dolphin HD
        if re.search(r'DolphinHDCN/([0-9.]*)', self.ua):
            self.browser['name'] = 'Dolphin'
            self.browser['version']['value'] = re.search(r'DolphinHDCN/([0-9.]*)', self.ua).group(1)
            self.device['type'] = 'mobile'
            if self.os.get('name', None) != 'Android':
                self.os['name'] = 'Android'
                self.os['version']['value'] = None
        if re.search(r'Dolphin/INT', self.ua):
            self.browser['name'] = 'Dolphin'
            self.device['type'] = 'mobile'

        # QQ Browser
        if re.search(r'(M?QQBrowser)/([0-9.]*)', self.ua):
            match = re.search(r'(M?QQBrowser)/([0-9.]*)', self.ua)
            self.browser['name'] = 'QQ Browser'

            version = match.group(2)
            if re.match(r'^[0-9][0-9]$', version):
                version = version[0] + '.' + version[1]

            self.browser['version']['value'] = version
            self.browser['version']['details'] = 2
            self.browser['channel'] = ''
            if not self.os.get('name', None) and match.group(1) == 'QQBrowser':
                self.os['name'] = 'Windows'

        # iBrowser
        if re.search(r'(iBrowser)/([0-9.]*)', self.ua):
            match = re.search(r'(iBrowser)/([0-9.]*)', self.ua)
            self.browser['name'] = 'iBrowser'
            version = match.group(2)
            if re.match(r'^[0-9][0-9]$', version):
                version = version[0] + '.' + version[1]
            self.browser['version']['value'] = version
            self.browser['version']['details'] = 2
            self.browser['channel'] = ''

        # Puffin
        if re.search(r'Puffin/([0-9.]*)', self.ua):
            self.browser['name'] = 'Puffin'
            self.browser['version']['value'] = re.search(r'Puffin/([0-9.]*)', self.ua).group(1)
            self.browser['version']['details'] = 2
            self.device['type'] = 'mobile'
            if self.os.get('name', None) == 'Linux':
                self.os['name'] = None
                self.os['version']['value'] = None

        # 360 Extreme Explorer
        if '360EE' in self.ua:
            self.browser['stock'] = False
            self.browser['name'] = '360 Extreme Explorer'
            self.browser['version']['value'] = None

        # Midori
        if re.search(r'Midori/([0-9.]*)', self.ua):
            self.browser['name'] = 'Midori'
            self.browser['version']['value'] = re.search(r'Midori/([0-9.]*)', self.ua).group(1)
            if self.os.get('name', None) != 'Linux':
                self.os['name'] = 'Linux'
                self.os['version']['value'] = None

            self.device['manufacturer'] = None
            self.device['model'] = None
            self.device['type'] = 'desktop'

        # Others
        for b in OTHER_BROWSERS:
            if 'flag' in b:
                match = re.search(b['regexp'], self.ua, b['flag'])
            else:
                match = re.search(b['regexp'], self.ua)
            if match:
                self.browser['name'] = b['name']
                self.browser['channel'] = ''
                self.browser['stock'] = False

                if len(match.groups()) > 0:
                    self.browser['version']['value'] = match.group(1)
                    self.browser['version']['details'] = b.get('details', None)
                else:
                    self.browser['version']['value'] = None

    def _parse_engine(self):
        # CMCC M811_LTE/1.0 Android/4.3 Release/26.5.2014 Browser/AppleWebKit534.30/Profile/MIDP-2.0 Configuration/CLDC-1.1
        # WebKit
        if re.search(r'WebKit/([0-9.]*)', self.ua, re.I):
            self.engine['name'] = 'WebKit'
            self.engine['version']['value'] = re.search(r'WebKit/([0-9.]*)', self.ua, re.I).group(1)

        if re.search(r'Browser/AppleWebKit([0-9.]*)', self.ua, re.I):
            self.engine['name'] = 'WebKit'
            self.engine['version']['value'] = re.search(r'Browser/AppleWebKit([0-9.]*)', self.ua, re.I).group(1)

        # KHTML
        if re.search(r'KHTML/([0-9.]*)', self.ua):
            self.engine['name'] = 'KHTML'
            self.engine['version']['value'] = re.search(r'KHTML/([0-9.]*)', self.ua).group(1)

        # Gecko
        if 'Gecko' in self.ua and not 'like gecko' in self.ua.lower():
            self.engine['name'] = 'Gecko'
            match = re.search(r'; rv:([^\)]+)\)', self.ua)
            if match:
                self.engine['version']['value'] = match.group(1)

        # Presto
        if re.search(r'Presto/([0-9.]*)', self.ua):
            self.engine['name'] = 'Presto'
            self.engine['version']['value'] = re.search(r'Presto/([0-9.]*)', self.ua).group(1)

        # Trident
        if re.search(r'Trident/([0-9.]*)', self.ua):
            match = re.search(r'Trident/([0-9.]*)', self.ua)
            self.engine['name'] = 'Trident'
            self.engine['version']['value'] = match.group(1)

            if self.browser.get('name', None) == 'Internet Explorer':
                if self.parse_version(self.engine['version']['value']) == 6 and self.parse_version(self.browser['version']['value']) < 10:
                    self.browser['version']['value'] = '10.0'
                    self.browser['mode'] = 'compat'

                if self.parse_version(self.engine['version']['value']) == 5 and self.parse_version(self.browser['version']['value']) < 9:
                    self.browser['version']['value'] = '9.0'
                    self.browser['mode'] = 'compat'

                if self.parse_version(self.engine['version']['value']) == 4 and self.parse_version(self.browser['version']['value']) < 8:
                    self.browser['version']['value'] = '8.0'
                    self.browser['mode'] = 'compat'

            if self.os.get('name', None) == 'Windows Phone':
                if self.parse_version(self.engine['version']['value']) == 5 and self.parse_version(self.os['version']['value']) < 7.5:
                    self.os['version']['value'] = '7.5'

    def _clear_camouflage(self):
        # Corrections
        if self.os.get('name', None) == 'Android' and self.browser.get('stock', False):
            self.browser['hidden'] = True

        if self.os.get('name', None) == 'iOS' and self.browser.get('name', None) == 'Opera Mini':
            self.os['version']['value'] = None

        if self.browser.get('name', None) == 'Midori' and self.engine.get('name', None) == 'Webkit':
            self.engine['name'] = 'Webkit'
            self.engine['version']['value'] = None

        if self.device.get('type', None) == 'television' and self.browser.get('name', None) == 'Opera':
            self.browser['name'] = 'Opera Devices'
            if self.engine['version']['value'] == '2.10':
                self.browser['version']['value'] = '3.2'
            elif self.engine['version']['value'] == '2.9':
                self.browser['version']['value'] = '3.1'
            elif self.engine['version']['value'] == '2.8':
                self.browser['version']['value'] = '3.0'
            elif self.engine['version']['value'] == '2.7':
                self.browser['version']['value'] = '2.9'
            elif self.engine['version']['value'] == '2.6':
                self.browser['version']['value'] = '2.8'
            elif self.engine['version']['value'] == '2.4':
                self.browser['version']['value'] = '10.3'
            elif self.engine['version']['value'] == '2.3':
                self.browser['version']['value'] = '10'
            elif self.engine['version']['value'] == '2.2':
                self.browser['version']['value'] = '9.7'
            elif self.engine['version']['value'] == '2.1':
                self.browser['version']['value'] = '9.6'
            else:
                self.browser['version']['value'] = None

            self.os['name'] = None
            self.os['version']['value'] = None

        # Camouflage
        if self.detect_camouflage:
            if re.search(r'Mac OS X 10_6_3; ([^;]+); [a-z]{2}-(?:[a-z]{2})?\)', self.ua):
                match = re.search(r'Mac OS X 10_6_3; ([^;]+); [a-z]{2}-(?:[a-z]{2})?\)', self.ua)
                self.browser['name'] = ''
                self.browser['version']['value'] = None
                self.browser['mode'] = 'desktop'

                self.os['name'] = 'Android'
                self.os['version']['value'] = None

                self.engine['name'] = 'Webkit'
                self.engine['version']['value'] = None

                self.device['model'] = match.group(1)
                self.device['type'] = 'mobile'

                model = self.cleanup_model(self.device['model'])
                if model in ANDROID_MODELS:
                    self.device['manufacturer'] = ANDROID_MODELS[model][0]
                    self.device['model'] = ANDROID_MODELS[model][1]
                    if len(ANDROID_MODELS[model]) > 2:
                        self.device['type'] = ANDROID_MODELS[model][2]
                    self.device['identified'] = True
                self.features.append('foundDevice')

            if re.search(r'Linux Ventana; [a-z]{2}-[a-z]{2}; (.+) Build', self.ua):
                match = re.search(r'Linux Ventana; [a-z]{2}-[a-z]{2}; (.+) Build', self.ua)
                self.browser['name'] = ''
                self.browser['version']['value'] = None
                self.browser['mode'] = 'desktop'

                self.os['name'] = 'Android'
                self.os['version']['value'] = None

                self.device['model'] = match.group(1)
                self.device['type'] = 'mobile'

                model = self.cleanup_model(self.devi['model'])
                if model in ANDROID_MODELS:
                    self.device['manufacturer'] = ANDROID_MODELS[model][0]
                    self.device['model'] = ANDROID_MODELS[model][1]
                    if len(ANDROID_MODELS[model]) > 2:
                        self.device['type'] = ANDROID_MODELS[model][2]
                    self.device['identified'] = True
                self.features.append('foundDevice')

    def _correct_device(self):
        match = None
        tmpMatch = None
        # handle mobile device
        if self.device.get('type', None) == 'mobile' or self.device.get('type', None) == 'tablet':
            # get manufacturer through the key words
            match = re.search(r'(ZTE|Samsung|Motorola|HTC|Coolpad|Huawei|Lenovo|LG|Sony Ericsson|Oppo|TCL|Vivo|Sony|Meizu|Nokia)', self.ua, re.I)
            if match:
                self.device['manufacturer'] = match.group(1)
                if self.device.get('model', False) and self.device['model'].find(match.group(1)) >= 0:
                    self.device['model'] = self.device['model'].replace(match.group(1), '')

            if re.search(r'(iPod|iPad|iPhone)', self.ua, re.I):
                # handle Apple
                # 苹果就这3种：iPod、iPad、iPhone
                match = re.search(r'(iPod|iPad|iPhone)', self.ua, re.I)
                self.device['manufacturer'] = 'Apple'
                self.device['model'] = match.group(1)
            elif re.search(r'[-\s](Galaxy[-\s_]nexus|Galaxy[-\s_]\w*[-\s_]\w*|Galaxy[-\s_]\w*|SM-\w*|GT-\w*|s[cgp]h-\w*|shw-\w*|ATIV|i9070|omnia|s7568|A3000|A3009|A5000|A5009|A7000|A7009|A8000|C101|C1116|C1158|E400|E500F|E7000|E7009|G3139D|G3502|G3502i|G3508|G3508J|G3508i|G3509|G3509i|G3558|G3559|G3568V|G3586V|G3589W|G3606|G3608|G3609|G3812|G388F|G5108|G5108Q|G5109|G5306W|G5308W|G5309W|G550|G600|G7106|G7108|G7108V|G7109|G7200|G720NO|G7508Q|G7509|G8508S|G8509V|G9006V|G9006W|G9008V|G9008W|G9009D|G9009W|G9198|G9200|G9208|G9209|G9250|G9280|I535|I679|I739|I8190N|I8262|I879|I879E|I889|I9000|I9060|I9082|I9082C|I9082i|I9100|I9100G|I9108|I9128|I9128E|I9128i|I9152|I9152P|I9158|I9158P|I9158V|I9168|I9168i|I9190|I9192|I9195|I9195I|I9200|I9208|I9220|I9228|I9260|I9268|I9300|I9300i|I9305|I9308|I9308i|I939|I939D|I939i|I9500|I9502|I9505|I9507V|I9508|I9508V|I959|J100|J110|J5008|J7008|N7100|N7102|N7105|N7108|N7108D|N719|N750|N7505|N7506V|N7508V|N7509V|N900|N9002|N9005|N9006|N9008|N9008S|N9008V|N9009|N9100|N9106W|N9108V|N9109W|N9150|N916|N9200|P709|P709E|P729|S6358|S7278|S7278U|S7562C|S7562i|S7898i|b9388)[\s\)]', self.ua, re.I):
                # handle Samsung
                # 特殊型号可能以xxx-开头 或者直接空格接型号 兼容build结尾或直接)结尾
                # Galaxy nexus才是三星 nexus是google手机
                # 三星手机类型：galaxy xxx|SM-xxx|GT-xxx|SCH-xxx|SGH-xxx|SPH-xxx|SHW-xxx  若这些均未匹配到，则启用在中关村在线爬取到的机型白名单进行判断
                match = re.search(r'([-\s](Galaxy[-\s_]nexus|Galaxy[-\s_]\w*[-\s_]\w*|Galaxy[-\s_]\w*|SM-\w*|GT-\w*|s[cgp]h-\w*|shw-\w*|ATIV|i9070|omnia|s7568|A3000|A3009|A5000|A5009|A7000|A7009|A8000|C101|C1116|C1158|E400|E500F|E7000|E7009|G3139D|G3502|G3502i|G3508|G3508J|G3508i|G3509|G3509i|G3558|G3559|G3568V|G3586V|G3589W|G3606|G3608|G3609|G3812|G388F|G5108|G5108Q|G5109|G5306W|G5308W|G5309W|G550|G600|G7106|G7108|G7108V|G7109|G7200|G720NO|G7508Q|G7509|G8508S|G8509V|G9006V|G9006W|G9008V|G9008W|G9009D|G9009W|G9198|G9200|G9208|G9209|G9250|G9280|I535|I679|I739|I8190N|I8262|I879|I879E|I889|I9000|I9060|I9082|I9082C|I9082i|I9100|I9100G|I9108|I9128|I9128E|I9128i|I9152|I9152P|I9158|I9158P|I9158V|I9168|I9168i|I9190|I9192|I9195|I9195I|I9200|I9208|I9220|I9228|I9260|I9268|I9300|I9300i|I9305|I9308|I9308i|I939|I939D|I939i|I9500|I9502|I9505|I9507V|I9508|I9508V|I959|J100|J110|J5008|J7008|N7100|N7102|N7105|N7108|N7108D|N719|N750|N7505|N7506V|N7508V|N7509V|N900|N9002|N9005|N9006|N9008|N9008S|N9008V|N9009|N9100|N9106W|N9108V|N9109W|N9150|N916|N9200|P709|P709E|P729|S6358|S7278|S7278U|S7562C|S7562i|S7898i|b9388)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Samsung'
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z]+[0-9]+[A-Z]*, 例如 G9006 G9006V 其实应该是G9006 另外三星只保留3位
                model = re.sub(re.compile(r'Galaxy S VI', re.I), 'Galaxy S6', match.group(1))
                model = re.sub(re.compile(r'Galaxy S V', re.I), 'Galaxy S5', model)
                model = re.sub(re.compile(r'Galaxy S IV', re.I), 'Galaxy S4', model)
                model = re.sub(re.compile(r'Galaxy s III', re.I), 'Galaxy S3', model)
                model = re.sub(re.compile(r'Galaxy S II', re.I), 'Galaxy S2', model)
                model = re.sub(re.compile(r'Galaxy S I', re.I), 'Galaxy S1', model)
                model = re.sub(re.compile(r'(?P<model>[a-z]+[0-9]{3})[0-9]?[a-z]*', re.I), lambda m:m.group('model'), model)
                self.device['model'] = model
            elif self.device['manufacturer'] and self.device['manufacturer'].lower() == 'samsung' and self.device.get('model', None):
                # 针对三星已经匹配出的数据做处理
                model = re.sub(re.compile(r'Galaxy S VI', re.I), 'Galaxy S6', self.device['model'])
                model = re.sub(re.compile(r'Galaxy S V', re.I), 'Galaxy S5', model)
                model = re.sub(re.compile(r'Galaxy S IV', re.I), 'Galaxy S4', model)
                model = re.sub(re.compile(r'Galaxy s III', re.I), 'Galaxy S3', model)
                model = re.sub(re.compile(r'Galaxy S II', re.I), 'Galaxy S2', model)
                model = re.sub(re.compile(r'Galaxy S I', re.I), 'Galaxy S1', model)
                model = re.sub(re.compile(r'(?P<model>[a-z]+[0-9]{3})[0-9]?[a-z]*', re.I), lambda m:m.group('model'), model)
                self.device['model'] = model
            elif re.search(r'(Huawei[-\s_](\w*[-_]?\w*)|\s(7D-\w*|ALE-\w*|ATH-\w*|CHE-\w*|CHM-\w*|Che1-\w*|Che2-\w*|D2-\w*|G616-\w*|G620S-\w*|G621-\w*|G660-\w*|G750-\w*|GRA-\w*|Hol-\w*|MT2-\w*|MT7-\w*|PE-\w*|PLK-\w*|SC-\w*|SCL-\w*|H60-\w*|H30-\w*)[\s\)])', self.ua, re.I):
                # handle Huawei
                # 兼容build结尾或直接)结尾
                # 华为机型特征：Huawei[-\s_](\w*[-_]?\w*)  或者以 7D-  ALE-  CHE-等开头
                match = re.search(r'(Huawei[-\s_](\w*[-_]?\w*)|\s(7D-\w*|ALE-\w*|ATH-\w*|CHE-\w*|CHM-\w*|Che1-\w*|Che2-\w*|D2-\w*|G616-\w*|G620S-\w*|G621-\w*|G660-\w*|G750-\w*|GRA-\w*|Hol-\w*|MT2-\w*|MT7-\w*|PE-\w*|PLK-\w*|SC-\w*|SCL-\w*|H60-\w*|H30-\w*)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Huawei'
                if len(match.groups()) >= 2 and match.group(2):
                    self.device['model'] = match.group(2)
                elif len(match.groups()) >= 3 and match.group(3):
                    self.device['model'] = match.group(3)
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：xxx-[A-Z][0-9]+ 例如  H30-L01  H30-L00  H30-L20  都应该是 H30-L
                # h30-l  h30-h  h30-t 都是H30
                match = re.search(r'(\w*)[-\s_]+[a-z0-9]+', self.device['model'], re.I)
                if match:
                    self.device['model'] = match.group(1)
            elif re.search(r';\s(mi|m1|m2|m3|m4|hm)(\s*\w*)[\s\)]', self.ua, re.I):
                # handle Xiaomi
                # 兼容build结尾或直接)结尾 以及特殊的HM处理方案(build/hm2013011)
                # xiaomi手机类型: mi m1 m2 m3 hm 开头
                # hongmi有特殊判断build/hm2015011
                match = re.search(r';\s(mi|m1|m2|m3|m4|hm)(\s*\w*)[\s\)]', self.ua, re.I)
                if re.search(r'(meitu|MediaPad)', self.ua, re.I):
                    # 美图手机名字冒充小米 比如 meitu m4 mizhi
                    tmpMatch = re.search(r'(meitu|MediaPad)', self.ua, re.I)
                    self.device['manufacturer'] = tmpMatch.group(1)
                    self.device['model'] = ''
                elif len(match.groups()) >= 2 and len(match.group(2)) > 0 and not re.search(r'\s', match.group(2)):
                    # 若匹配出的 match[2]没空格 会出现很多例如 mizi mizhi miha 但也会出现mi3 minote之类 特殊处理下
                    tmpMatch = re.search(r'(\d)', match.group(2), re.I)
                    if tmpMatch:
                        self.device['model'] = match.group(1) + '-' + tmpMatch.group(1)
                else:
                    self.device['manufacturer'] = 'Xiaomi'
                    if len(match.groups()) >= 2 and len(match.group(2)) > 0:
                        m = re.sub(r'\s', '', match.group(2))
                        self.device['model'] = re.sub(re.compile(r'm(?P<number>\d)-', re.I), lambda v: 'MI-%d' % int(v.group('number')), match.group(1)[-2:] + '-' + m)
                    else:
                        self.device['model'] = re.sub(re.compile(r'm(?P<number>\d)', re.I), lambda v: 'MI-%d' % int(v.group('number')), match.group(1)[-2:])

                    # 解决移动联通等不同发行版导致的机型不同问题
                    # 特征：mi-3c,例如mi-4LTE mi-4 其实应该是 mi-4
                    if re.search(r'(mi|hm)(-\d)', self.device.get('model', ''), re.I):
                        if re.search(r'(mi|hm)(-\ds)', self.device.get('model', ''), re.I):
                            # 看看是不是 MI-3S  MI-4S....
                            match = re.search(r'(mi|hm)(-\ds)', self.device.get('model', ''), re.I)
                            self.device['model'] = match.group(1) + match.group(2)
                        elif re.search(r'(mi|hm)(-\d{2})', self.device.get('model', ''), re.I):
                            # 防止 MI-20150XX等滥竽充数成为MI-2
                            match = re.search(r'(mi|hm)(-\d{2})', self.device.get('model', ''), re.I)
                            self.device['model'] = match.group(1)
                        elif re.search(r'(mi|hm)(-\d)[A-Z]', self.device.get('model', ''), re.I):
                            # 将mi-3c mi-3a mi-3w等合为mi-3
                            match = re.search(r'(mi|hm)(-\d)[A-Z]', self.device.get('model', ''), re.I)
                            self.device['model'] = match.group(1) + match.group(2)

                    # 去除 mi-4g这样的东西
                    match = re.search(r'(mi|hm)(-\dg)', self.device.get('model', ''), re.I)
                    if match:
                        self.device['model'] = match.group(1)
            elif re.search(r'build/HM\d{0,7}\)', self.ua, re.I):
                self.device['manufacturer'] = 'Xiaomi'
                self.device['model'] = 'HM'
            elif self.device['manufacturer'] and self.device['manufacturer'].lower() == 'xiaomi' and self.device.get('model', False):
                # 针对通过base库判断出数据时命名风格不同。特殊处理适配如下
                if re.search(r'mi-one', self.device['model'], re.I):
                    self.device['model'] = 'MI-1'
                elif re.search(r'mi-two', self.device['model'], re.I):
                    # mi 2
                    self.device['model'] = 'MI-2'
                elif re.search(r'\d{6}', self.device['model'], re.I):
                    # 20150xxx2014501
                    self.device['model'] = ''
                elif re.search(r'redmi', self.device['model'], re.I):
                    self.device['model'] = re.sub(re.compile(r'redmi', re.I), 'HM', self.device['model'].upper())
                elif re.search(r'(m\d)[-\s_](s?)', self.device['model'], re.I):
                    # m1 m2 m3 写法不标准 另外判断是否是 m1-s
                    match = re.search(r'(m\d)[-\s_](s?)', self.device['model'], re.I)
                    self.device['model'] = re.sub(r'm', 'MI-', match.group(1))
                elif re.search(r'(hm|mi)[-\s_](\d?)[a-rt-z]', self.device['model'], re.I):
                    # mi-2w  mi-3w 等格式化为mi-2  mi-3
                    match = re.search(r'(hm|mi)[-\s_](\d?)[a-rt-z]', self.device['model'], re.I)
                    tmpMatch = re.search(r'(mi|hm)[-\s_](note|pad)(\d?s?)', self.device['model'], re.I)
                    if tmpMatch:
                        self.device['model'] = tmpMatch.group(1) + '-' + tmpMatch.group(2) + tmpMatch.group(3)
                    else:
                        self.device['model'] = match.group(1) + '-' + match.group(2) if len(match.groups()) >= 2 else match.group(1)
                elif re.search(r'hm', self.device['model'], re.I):
                    # 处理hm
                    if re.search(r'(hm)[-\s_](\d{2})', self.device['model'], re.I):
                        # 判断是不是 hm-201xxx充数
                        self.device['model'] = 'HM'
                    elif re.search(r'(hm)[-\s_](\ds)', self.device['model'], re.I):
                        # 判断是不是 hm-2s hm-1s
                        match = re.search(r'(hm)[-\s_](\ds)', self.device['model'], re.I)
                        self.device['model'] = 'HM-%s' % match.group(2)
                    elif re.search(r'(hm)[-\s_](\d)[a-z]', self.device['model'], re.I):
                        match = re.search(r'(hm)[-\s_](\d)[a-z]', self.device['model'], re.I)
                        self.device['model'] = 'HM-%s' % match.group(2)
                    else:
                        self.device['model'] = 'HM'
                    if re.search(r'hm-\dg', self.device['model']):
                        # 过滤类似 2g 3g等数据
                        self.device['model'] = 'HM'
            elif re.search(r'(vivo[-\s_](\w*)|\s(E1\w?|E3\w?|E5\w?|V1\w?|V2\w?|S11\w?|S12\w?|S1\w?|S3\w?|S6\w?|S7\w?|S9\w?|X1\w?|X3\w?|X520\w?|X5\w?|X5Max|X5Max+|X5Pro|X5SL|X710F|X710L|Xplay|Xshot|Xpaly3S|Y11\w?|Y11i\w?|Y11i\w?|Y13\w?|Y15\w?|Y17\w?|Y18\w?|Y19\w?|Y1\w?|Y20\w?|Y22\w?|Y22i\w?|Y23\w?|Y27\w?|Y28\w?|Y29\w?|Y33\w?|Y37\w?|Y3\w?|Y613\w?|Y622\w?|Y627\w?|Y913\w?|Y923\w?|Y927\w?|Y928\w?|Y929\w?|Y937\w?)[\s\)])', self.ua, re.I):
                # handle Vivo
                # 兼容build结尾或直接)结尾
                # vivo机型特征: Vivo[-\s_](\w*)  或者以 E1  S11t  S7t 等开头
                match = re.search(r'(vivo[-\s_](\w*)|\s(E1\w?|E3\w?|E5\w?|V1\w?|V2\w?|S11\w?|S12\w?|S1\w?|S3\w?|S6\w?|S7\w?|S9\w?|X1\w?|X3\w?|X520\w?|X5\w?|X5Max|X5Max+|X5Pro|X5SL|X710F|X710L|Xplay|Xshot|Xpaly3S|Y11\w?|Y11i\w?|Y11i\w?|Y13\w?|Y15\w?|Y17\w?|Y18\w?|Y19\w?|Y1\w?|Y20\w?|Y22\w?|Y22i\w?|Y23\w?|Y27\w?|Y28\w?|Y29\w?|Y33\w?|Y37\w?|Y3\w?|Y613\w?|Y622\w?|Y627\w?|Y913\w?|Y923\w?|Y927\w?|Y928\w?|Y929\w?|Y937\w?)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Vivo'
                self.device['model'] = match.group(1)
                # 首先剔除 viv-  vivo-  bbg- 等打头的内容
                self.device['model'] = re.sub(re.compile(r'(viv[-\s_]|vivo[-\s_]|bbg[-\s_])', re.I), '', self.device['model'])
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  X5F X5L X5M X5iL 都应该是 X5
                match = re.search(r'([a-z]+[0-9]+)i?[a-z]?[-\s_]?', self.device['model'], re.I)
                if match:
                    self.device['model'] = match.group(1)
            elif re.search(r'(Oppo[-\s_](\w*)|\s(1100|1105|1107|3000|3005|3007|6607|A100|A103|A105|A105K|A109|A109K|A11|A113|A115|A115K|A121|A125|A127|A129|A201|A203|A209|A31|A31c|A31t|A31u|A51kc|A520|A613|A615|A617|E21W|Find|Mirror|N5110|N5117|N5207|N5209|R2010|R2017|R6007|R7005|R7007|R7c|R7t|R8000|R8007|R801|R805|R807|R809T|R8107|R8109|R811|R811W|R813T|R815T|R815W|R817|R819T|R8200|R8205|R8207|R821T|R823T|R827T|R830|R830S|R831S|R831T|R833T|R850|Real|T703|U2S|U521|U525|U529|U539|U701|U701T|U705T|U705W|X9000|X9007|X903|X905|X9070|X9077|X909|Z101|R829T)[\s\)])', self.ua, re.I):
                # handle Oppo
                match = re.search(r'(Oppo[-\s_](\w*)|\s(1100|1105|1107|3000|3005|3007|6607|A100|A103|A105|A105K|A109|A109K|A11|A113|A115|A115K|A121|A125|A127|A129|A201|A203|A209|A31|A31c|A31t|A31u|A51kc|A520|A613|A615|A617|E21W|Find|Mirror|N5110|N5117|N5207|N5209|R2010|R2017|R6007|R7005|R7007|R7c|R7t|R8000|R8007|R801|R805|R807|R809T|R8107|R8109|R811|R811W|R813T|R815T|R815W|R817|R819T|R8200|R8205|R8207|R821T|R823T|R827T|R830|R830S|R831S|R831T|R833T|R850|Real|T703|U2S|U521|U525|U529|U539|U701|U701T|U705T|U705W|X9000|X9007|X903|X905|X9070|X9077|X909|Z101|R829T)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Oppo'
                if len(match.groups()) >= 2 and match.group(2):
                    self.device['model'] = match.group(2)
                elif len(match.groups()) >= 3 and match.group(3):
                    self.device['model'] = match.group(3)
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  A31c A31s 都应该是 A31
                # 对 Plus 做特殊处理
                if re.search(r'([a-z]+[0-9]+)-?(plus)', self.device['model'], re.I):
                    match = re.search(r'([a-z]+[0-9]+)-?(plus)', self.device['model'], re.I)
                    self.device['model'] = match.group(1) + '-' + match.group(2)
                elif re.search(r'(\w*-?[a-z]+[0-9]+)', self.device['model'], re.I):
                    match = re.search(r'(\w*-?[a-z]+[0-9]+)', self.device['model'], re.I)
                    self.device['model'] = match.group(1)
            elif self.device['manufacturer'] and self.device['manufacturer'].lower() == 'oppo' and self.device.get('model', False):
                # 针对base库的数据做数据格式化处理
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  A31c A31s 都应该是 A31
                # 对 Plus 做特殊处理
                if re.search(r'([a-z]+[0-9]+)-?(plus)', self.device['model'], re.I):
                    match = re.search(r'([a-z]+[0-9]+)-?(plus)', self.device['model'], re.I)
                    self.device['model'] = match.group(1) + '-' + match.group(2)
                elif re.search(r'(\w*-?[a-z]+[0-9]+)', self.device['model'], re.I):
                    match = re.search(r'(\w*-?[a-z]+[0-9]+)', self.device['model'], re.I)
                    self.device['model'] = match.group(1)
            elif re.search(r'(Lenovo[-\s_](\w*[-_]?\w*)|\s(A3580|A3860|A5500|A5600|A5860|A7600|A806|A800|A808T|A808T-I|A936|A938t|A788t|K30-E|K30-T|K30-W|K50-T3s|K50-T5|K80M|K910|K910e|K920|S90-e|S90-t|S90-u|S968T|X2-CU|X2-TO|Z90-3|Z90-7)[\s\)])', self.ua, re.I):
                # handle Lenovo
                # 兼容build结尾或直接)结尾 兼容Lenovo-xxx/xxx以及Leveno xxx build等
                match = re.search(r'(Lenovo[-\s_](\w*[-_]?\w*)|\s(A3580|A3860|A5500|A5600|A5860|A7600|A806|A800|A808T|A808T-I|A936|A938t|A788t|K30-E|K30-T|K30-W|K50-T3s|K50-T5|K80M|K910|K910e|K920|S90-e|S90-t|S90-u|S968T|X2-CU|X2-TO|Z90-3|Z90-7)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Lenovo'
                if len(match.groups()) >= 2 and match.group(2):
                    self.device['model'] = match.group(2)
                elif len(match.groups()) >= 3 and match.group(3):
                    self.device['model'] = match.group(3)
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  A360t A360 都应该是 A360
                match = re.search(r'([a-z]+[0-9]+)', self.device['model'], re.I)
                if match:
                    self.device['model'] = match.group(1)
            elif re.search(r'(Coolpad[-\s_](\w*)|\s(7295C|7298A|7620L|8908|8085|8970L|9190L|Y80D)[\s\)])', self.ua, re.I):
                # handle coolpad
                match = re.search(r'(Coolpad[-\s_](\w*)|\s(7295C|7298A|7620L|8908|8085|8970L|9190L|Y80D)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Coolpad'
                if len(match.groups()) >= 2 and match.group(2):
                    self.device['model'] = match.group(2)
                elif len(match.groups()) >= 3 and match.group(3):
                    self.device['model'] = match.group(3)
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  8297-t01 8297-c01 8297w 都应该是 8297
                match = re.search(r'([a-z]?[0-9]+)', self.device['model'], re.I)
                if match:
                    self.device['model'] = match.group(1)
            elif self.device.get('manufacturer', False) and self.device['manufacturer'].lower() == 'coolpad' and self.device.get('model', False):
                # base 库适配
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  8297-t01 8297-c01 8297w 都应该是 8297
                match = re.search(r'([a-z]?[0-9]+)', self.device['model'], re.I)
                if match:
                    self.device['model'] = match.group(1)
            elif re.search(r'\s(mx\d*\w*|mz-(\w*))\s(\w*)\s*\w*\s*build', self.ua, re.I):
                # handle meizu
                match = re.search(r'\s(mx\d*\w*|mz-(\w*))\s(\w*)\s*\w*\s*build', self.ua, re.I)
                self.device['manufacturer'] = 'Meizu'
                tmpModel = match.group(2) if match.group(2) else match.group(1)
                if match.group(3):
                    self.device['model'] = tmpModel + '-' + match.group(3)
                else:
                    self.device['model'] = tmpModel + '';
            elif re.search(r'(M463C|M35)\d', self.ua, re.I):
                match = re.search(r'(M463C|M35)\d', self.ua, re.I)
                self.device['manufacturer'] = 'Meizu'
                self.device['model'] = match.group(1)
            elif re.search(r'(Htc[-_\s](\w*)|\s(601e|606w|608t|609d|610t|6160|619d|620G|626d|626s|626t|626w|709d|801e|802d|802t|802w|809D|816d|816e|816t|816v|816w|826d|826s|826t|826w|828w|901e|919d|A310e|A50AML|A510e|A620d|A620e|A620t|A810e|A9191|Aero|C620d|C620e|C620t|D316d|D516d|D516t|D516w|D820mt|D820mu|D820t|D820ts|D820u|D820us|E9pt|E9pw|E9sw|E9t|HD7S|M8Et|M8Sd|M8St|M8Sw|M8d|M8e|M8s|M8si|M8t|M8w|M9W|M9ew|Phablet|S510b|S510e|S610d|S710d|S710e|S720e|S720t|T327t|T328d|T328t|T328w|T329d|T329t|T329w|T528d|T528t|T528w|T8698|WF5w|X315e|X710e|X715e|X720d|X920e|Z560e|Z710e|Z710t|Z715e)[\s\)])', self.ua):
                match = re.search(r'(Htc[-_\s](\w*)|\s(601e|606w|608t|609d|610t|6160|619d|620G|626d|626s|626t|626w|709d|801e|802d|802t|802w|809D|816d|816e|816t|816v|816w|826d|826s|826t|826w|828w|901e|919d|A310e|A50AML|A510e|A620d|A620e|A620t|A810e|A9191|Aero|C620d|C620e|C620t|D316d|D516d|D516t|D516w|D820mt|D820mu|D820t|D820ts|D820u|D820us|E9pt|E9pw|E9sw|E9t|HD7S|M8Et|M8Sd|M8St|M8Sw|M8d|M8e|M8s|M8si|M8t|M8w|M9W|M9ew|Phablet|S510b|S510e|S610d|S710d|S710e|S720e|S720t|T327t|T328d|T328t|T328w|T329d|T329t|T329w|T528d|T528t|T528w|T8698|WF5w|X315e|X710e|X715e|X720d|X920e|Z560e|Z710e|Z710t|Z715e)[\s\)])', self.ua)
                self.device['manufacturer'] = 'Htc'
                self.device['model'] = match.group(1)
            elif re.search(r'(Gionee[-\s_](\w*)|\s(GN\d+\w*)[\s\)])', self.ua, re.I):
                # handle Gionee
                self.device['manufacturer'] = 'GinDream'
                match = re.search(r'(Gionee[-\s_](\w*)|\s(GN\d+\w*)[\s\)])', self.ua, re.I)
                if match.group(2):
                    self.device['model'] = match.group(2)
                elif match.group(3):
                    self.device['model'] = match.group(3)
            elif re.search(r'(LG[-_](\w*)|\s(D728|D729|D802|D855|D856|D857|D858|D859|E985T|F100L|F460|H778|H818|H819|P895|VW820)[\s\)])', self.ua, re.I):
                # handle LG
                match = re.search(r'(LG[-_](\w*)|\s(D728|D729|D802|D855|D856|D857|D858|D859|E985T|F100L|F460|H778|H818|H819|P895|VW820)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Lg'
                if match.group(2):
                    self.device['model'] = match.group(2)
                elif match.group(3):
                    self.device['model'] = match.group(3)
            elif re.search(r'(Tcl[-\s_](\w*)|\s(H916T|P588L|P618L|P620M|P728M)[\s\)])', self.ua):
                match = re.search(r'(Tcl[-\s_](\w*)|\s(H916T|P588L|P618L|P620M|P728M)[\s\)])', self.ua)
                self.device['manufacturer'] = 'Tcl'
                self.device['model'] = match.group(1)
            elif re.search(r'(V9180|N918)', self.ua, re.I):
                # ZTE
                match = re.search(r'(V9180|N918)', self.ua, re.I)
                self.device['manufacturer'] = 'Zte'
                self.device['model'] = match.group(1)
            elif self.device.get('manufacturer', False) and self.device['manufacturer'].lower() == 'zte' and self.device.get('model', False):
                # base 库适配
                # 解决移动联通等不同发行版导致的机型不同问题
                # 特征：[A-Z][0-9]+[A-Z] 例如  Q505T Q505u 都应该是 Q505
                match = re.search(r'([a-z]?[0-9]+)', self.device['model'], re.I)
                if match:
                    self.device['model'] = match.group(1)
            elif re.search(r'(UIMI\w*|umi\w*)[-\s_](\w*)\s*\w*\s*build', self.ua, re.I):
                # UIMI
                match = re.search(r'(UIMI\w*|umi\w*)[-\s_](\w*)\s*\w*\s*build', self.ua, re.I)
                self.device['manufacturer'] = 'Uimi'
                if match.group(2):
                    self.device['model'] = match.group(1) + '-' + match.group(2)
                else:
                    self.device['model'] = match.group(1) + ''
            elif re.search(r'eton[-\s_](\w*)', self.ua, re.I):
                # eton
                match = re.search(r'eton[-\s_](\w*)', self.ua, re.I)
                self.device['manufacturer'] = 'Eton'
                self.device['model'] = match.group(1)
            elif re.search(r'(SM705|SM701|YQ601|YQ603)', self.ua, re.I):
                # Smartisan
                match = re.search(r'(SM705|SM701|YQ601|YQ603)', self.ua, re.I)
                self.device['manufacturer'] = 'Smartisan'
                self.device['model'] = {'SM705':'T1', 'SM701':'T1', 'YQ601':'U1', 'YQ603':'U1'}.get(match.group(1), match.group(1))
            elif re.search(r'(Asus[-\s_](\w*)|\s(A500CG|A500KL|A501CG|A600CG|PF400CG|PF500KL|T001|X002|X003|ZC500TG|ZE550ML|ZE551ML)[\s\)])', self.ua, re.I):
                # handle Asus
                match = re.search(r'(Asus[-\s_](\w*)|\s(A500CG|A500KL|A501CG|A600CG|PF400CG|PF500KL|T001|X002|X003|ZC500TG|ZE550ML|ZE551ML)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Asus'
                if match.group(2):
                    self.device['model'] = match.group(2)
                elif match.group(3):
                    self.device['model'] = match.group(3)
            elif re.search(r'(Nubia[-_\s](\w*)|(NX501|NX505J|NX506J|NX507J|NX503A|nx\d+\w*)[\s\)])', self.ua, re.I):
                # handle nubia
                match = re.search(r'(Nubia[-_\s](\w*)|(NX501|NX505J|NX506J|NX507J|NX503A|nx\d+\w*)[\s\)])', self.ua, re.I)
                self.device['manufacturer'] = 'Nubia'
                if match.group(2):
                    self.device['model'] = match.group(2)
                elif match.group(3):
                    self.device['model'] = match.group(3)
            elif re.search(r'(HT-\w*)|Haier[-\s_](\w*-?\w*)', self.ua, re.I):
                # handle haier
                match = re.search(r'(HT-\w*)|Haier[-\s_](\w*-?\w*)', self.ua, re.I)
                self.device['manufacturer'] = 'Haier'
                if match.group(1):
                    self.device['model'] = match.group(1)
                elif match.group(2):
                    self.device['model'] = match.group(2)
            elif re.search(r'K-Touch[-\s_](tou\s?ch\s?(\d)|\w*)', self.ua, re.I):
                # tianyu
                match = re.search(r'K-Touch[-\s_](tou\s?ch\s?(\d)|\w*)', self.ua, re.I)
                self.device['manufacturer'] = 'K-Touch'
                if match.group(2):
                    self.device['model'] = 'Ktouch' + match.group(2)
                else:
                    self.device['model'] = match.group(1)
            elif re.search(r'Doov[-\s_](\w*)', self.ua, re.I):
                # DOOV
                match = re.search(r'Doov[-\s_](\w*)', self.ua, re.I)
                self.device['manufacturer'] = 'Doov'
                self.device['model'] = match.group(1)
            elif re.search(r'koobee', self.ua, re.I):
                # coobee
                self.device['manufacturer'] = 'koobee'
            elif re.search(r'C69', self.ua, re.I):
                # sony
                self.device['manufacturer'] = 'Sony'
            elif re.search(r'N787|N818S', self.ua, re.I):
                # haojixing
                self.device['manufacturer'] = 'Haojixing'
            elif re.search(r'(hs-|Hisense[-\s_])(\w*)', self.ua, re.I):
                # haojixing
                match = re.search(r'(hs-|Hisense[-\s_])(\w*)', self.ua, re.I)
                self.device['manufacturer'] = 'Hisense'
                self.device['model'] = match.group(2)

            # format the style of manufacturer
            if self.device.get('manufacturer', False):
                self.device['manufacturer'] = self.device['manufacturer'].capitalize()

            # format the style of model
            if self.device.get('model', False):
                model = re.sub(r'-+|_+|\s+', ' ', self.device['model'].upper())
                model = re.search(r'\s*(\w*\s*\w*)', model).group(1)
                model = re.sub(r'\s+', '-', model)
                self.device['model'] = model

                # 针对三星、华为做去重的特殊处理
                if self.device.get('manufacturer', '') == 'Samsung':
                    self.device['model'] = {
                        'SCH-I95': 'GT-I950',
                        'SCH-I93': 'GT-I930',
                        'SCH-I86': 'GT-I855',
                        'SCH-N71': 'GT-N710',
                        'SCH-I73': 'GT-S789',
                        'SCH-P70': 'GT-I915'
                    }.get(self.device['model'], self.device['model'])
                elif self.device.get('manufacturer', '') == 'Huawei':
                    self.device['model'] = {
                        'CHE1': 'CHE',
                        'CHE2': 'CHE',
                        'G620S': 'G621',
                        'C8817D': 'G621'
                    }.get(self.device['model'], self.device['model'])

            # 针对xiaomi 的部分数据没有格式化成功，格式化1次
            if self.device.get('manufacturer', '') == 'Xiaomi':
                if re.search(r'(hm|mi)-(note)', self.device['model'], re.I):
                    match = re.search(r'(hm|mi)-(note)', self.device['model'], re.I)
                    self.device['model'] = match.group(1) + '-' + match.group(2)
                elif re.search(r'(hm|mi)-(\ds?)', self.device['model'], re.I):
                    match = re.search(r'(hm|mi)-(\ds?)', self.device['model'], re.I)
                    self.device['model'] = match.group(1) + '-' + match.group(2)
                elif re.search(r'(hm|mi)-(\d)[a-rt-z]', self.device['model'], re.I):
                    match = re.search(r'(hm|mi)-(\d)[a-rt-z]', self.device['model'], re.I)
                    self.device['model'] = match.group(1) + '-' + match.group(2)

    def _correct_browser(self):
        match = None
        tmpMatch = None
        if self.device.get('type', '') == 'desktop':
            if re.search(r'360se(?:[ /]([\w.]+))?', self.ua, re.I):
                # 360 security Explorer
                match = re.search(r'360se(?:[ /]([\w.]+))?', self.ua, re.I)
                self.browser['name'] = '360 security Explorer'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'the world(?:[ /]([\w.]+))?', self.ua, re.I):
                # the world
                match = re.search(r'the world(?:[ /]([\w.]+))?', self.ua, re.I)
                self.browser['name'] = 'the world'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'tencenttraveler ([\w.]+)', self.ua, re.I):
                # tencenttraveler
                match = re.search(r'tencenttraveler ([\w.]+)', self.ua, re.I)
                self.browser['name'] = 'tencenttraveler'
                self.browser['version']['original'] = match.group(1)
        elif self.device.get('type', '') == 'mobile' or self.device.get('type', '') == 'tablet':
            if re.search(r'BaiduHD\s+([\w.]+)', self.ua, re.I):
                # BaiduHD
                match = re.search(r'BaiduHD\s+([\w.]+)', self.ua, re.I)
                self.browser['name'] = 'BaiduHD'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'360.s*aphone\s*browser\s*\(version\s*([\w.]+)\)', self.ua, re.I):
                # 360 Browser
                match = re.search(r'360.s*aphone\s*browser\s*\(version\s*([\w.]+)\)', self.ua, re.I)
                self.browser['name'] = '360 Browser'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'flyflow\/([\w.]+)', self.ua, re.I):
                # Baidu Browser
                match = re.search(r'flyflow\/([\w.]+)', self.ua, re.I)
                self.browser['name'] = 'Baidu Browser'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'baiduhd ([\w.]+)', self.ua, re.I):
                # Baidu HD
                match = re.search(r'baiduhd ([\w.]+)', self.ua, re.I)
                self.browser['name'] = 'Baidu HD'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'LieBaoFast/([\w.]+)', self.ua, re.I):
                # LieBaoFast
                match = re.search(r'LieBaoFast/([\w.]+)', self.ua, re.I)
                self.browser['name'] = 'LieBao Fast'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'LieBao/([\w.]+)', self.ua, re.I):
                # LieBao
                match = re.search(r'LieBao/([\w.]+)', self.ua, re.I)
                self.browser['name'] = 'LieBao'
                self.browser['version']['original'] = match.group(1)
            elif self.os.get('name', '') == 'Android' and re.search(r'safari', self.ua, re.I) and re.search(r'version/([0-9\.]+)', self.ua, re.I):
                # Android Google Browser
                match = re.search(r'version/([0-9\.]+)', self.ua, re.I)
                self.browser['name'] = 'Google Browser'
                self.browser['version']['original'] = match.group(1)
            elif re.search(r'(ipad|iphone).* applewebkit/.* mobile', self.ua, re.I):
                # 'Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B206' belongs to Safari
                self.browser['name'] = 'Safari'

        if re.search(r'baiduboxapp', self.ua, re.I):
            self.browser['name'] = '百度框'
        elif re.search(r'BaiduLightAppRuntime', self.ua, re.I):
            self.browser['name'] = '轻应用runtime'
        elif re.search(r'Weibo', self.ua, re.I):
            self.browser['name'] = '微博'
        elif re.search(r'MQQ', self.ua, re.I):
            self.browser['name'] = '手机QQ'
        elif re.search(r'hao123', self.ua, re.I):
            self.browser['name'] = 'hao123'

        match = re.search(r'MicroMessenger/([\w.]+)', self.ua, re.I)
        if match:
            self.browser['name'] = '微信'
            tmpVersion = re.sub(r'_', '.', match.group(1))
            tmpMatch = re.search(r'(\d+\.\d+\.\d+\.\d+)', tmpVersion)
            if tmpMatch:
                tmpVersion = tmpMatch.group(1)
            self.browser['version']['original'] = tmpVersion

        match = re.search(r'UCBrowser/([\w.]+)', self.ua, re.I)
        if match:
            self.browser['name'] = 'UC Browser'
            self.browser['version']['original'] = match.group(1)

        if re.search(r'OPR/([\w.]+)', self.ua, re.I):
            match = re.search(r'OPR/([\w.]+)', self.ua, re.I)
            self.browser['name'] = 'Opera'
            self.browser['version']['original'] = match.group(1)
        elif re.search(r'Trident/7', self.ua, re.I) and re.search(r'rv:11', self.ua, re.I):
            # IE 11
            self.browser['name'] = 'Internet Explorer'
            self.browser['version']['major'] = '11'
            self.browser['version']['original'] = '11'
        elif re.search(r'Edge/12', self.ua, re.I) and re.search(r'Windows Phone|Windows NT', self.ua, re.I):
            # Microsoft Edge
            self.browser['name'] = 'Microsoft Edge'
            self.browser['version']['major'] = '12'
            self.browser['version']['original'] = '12'
        elif re.search(r'miuibrowser/([\w.]+)', self.ua, re.I):
            # miui browser
            match = re.search(r'miuibrowser/([\w.]+)', self.ua, re.I)
            self.browser['name'] = 'miui browser'
            self.browser['version']['original'] = match.group(1)
        if not self.browser.get('name', False):
            if re.search(r'Safari/([\w.]+)', self.ua, re.I) and re.search(r'Version', self.ua, re.I):
                self.browser['name'] = 'Safari'

        if self.browser['name'] and not self.browser['version']['value'] and len(self.browser['version']) == 1:
            match = re.search(r'Version/([\w.]+)', self.ua, re.I)
            if match:
                self.browser['version']['original'] = match.group(1)

    def _correct_os(self):
        match = None
        tmpMatch = None
        # handle os
        if self.os.get('name', '') == 'Windows' or re.search(r'Windows', self.ua, re.I):
            self.os['name'] = 'Windows'
            if re.search(r'NT 6.3', self.ua, re.I):
                self.os['version']['alias'] = '8.1'
                self.os['version']['original'] = '8.1'
            elif re.search(r'NT 6.4', self.ua, re.I) or re.search(r'NT 10.0', self.ua, re.I):
                self.os['version']['alias'] = '10'
                self.os['version']['original'] = '10'
        elif self.os.get('name', '') == 'Mac OS X':
            self.os['name'] = 'Mac OS X'
            match = re.search(r'Mac OS X[\s\_\-\/](\d+[\.\-\_]\d+[\.\-\_]?\d*)', self.ua, re.I)
            if match:
                self.os['version']['alias'] = re.sub(r'_', '.', match.group(1))
                self.os['version']['original'] = re.sub(r'_', '.', match.group(1))
            else:
                self.os['version']['alias'] = ''
                self.os['version']['original'] = ''
        elif re.search(r'Android', self.os.get('name', ''), re.I):
            match = re.search(r'Android[\s\_\-\/i686]?[\s\_\-\/](\d+[\.\-\_]\d+[\.\-\_]?\d*)', self.ua, re.I)
            if match:
                self.os['version']['alias'] = match.group(1)
                self.os['version']['original'] = match.group(1)

    def _parse(self):
        self._parse_os_and_device()
        self._parse_browser()
        self._parse_engine()
        self._clear_camouflage()

    def _correct(self):
        self._correct_device()
        self._correct_browser()
        self._correct_os()

    def reset(self):
        self.ua = ''
        self.os = {
            'name' : None,
            'version' : {
                'value' : None
            },
        }
        self.engine = {
            'name' : None,
            'version' : {
                'value' : None
            },
        }
        self.browser = {
            'name' : None,
            'version' : {
                'value' : None
            },
            'mode' : '',
        }
        self.device = {
            'model' : None,
            'manufacturer' : None,
            'category' : None,
        }

    def detect(self):
        self._parse();
        self._correct();
        userAgent = UserAgent();
        userAgent.set_os(self.os);
        userAgent.set_engine(self.engine);
        userAgent.set_browser(self.browser);
        userAgent.set_device(self.device);
        return userAgent;
