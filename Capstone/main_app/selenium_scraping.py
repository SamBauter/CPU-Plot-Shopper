from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import numpy as np

monitor_col_header = ['brand', 'model', 'size', 'resolution', 'ref_rate', 'res_rate', 'panel_type', 'asp_ratio',
                      'price']
cpu_col_header = ['brand', 'model', 'core_count', 'core_clock', 'boost_clock', 'tdp', 'integrated_graphics', 'smt',
                  'price']
gpu_col_header = ['brand', 'model', 'chipset', 'memory', 'core_clock', 'boost_clock', 'color', 'length',
                  'price']

ram_col_header = ['brand', 'model', 'speed', 'modules', 'price_per_gb', 'color', 'first_word_lat', 'cas_lat',
                  'price']
motherboard_col_header = ['brand', 'model', 'socket', 'form_factor', 'mem_max', 'mem_slots', 'color',
                          'price']

psu_col_header = ['brand', 'model', 'form_factor', 'eff_rating', 'wattage', 'modular', 'color',
                  'price']

stor_col_header = ['brand', 'model', 'capacity', 'price_per_gb', 'type', 'cache', 'form_factor', 'interface',
                   'price']


# must update range based on num of specs 5 or 6 meaning range (1,6) or (1,7)
def checkForEmpties(products_list):
    list_of_spec_lists = []
    for entry in products_list:
        entry_spec = []
        for i in range(1, 7):
            spec_xpath = ".//td[@class='td__spec td__spec--" + str(i) + "']"
            try:
                single_spec = entry.find_element_by_xpath(spec_xpath)
                single_spec = single_spec.text
                # spec = entry.find_element_by_xpath("//td[@class='td__spec td__spec--1']")
            except NoSuchElementException:
                # print("An Empty was found")
                single_spec = ""
            entry_spec.append(single_spec)
        list_of_spec_lists.append(entry_spec)
    return list_of_spec_lists


# must comment out spec 6 and remove it from zipped info var if you have only 5 specs
def get_browser_after_POST(base_url="https://pcpartpicker.com/products/monitor/"):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path="venv/chromedriver-Darwin", chrome_options=option)
    browser.get(base_url)

    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='td__price']")))
    except TimeoutException:
        print("Timed out waiting for page to load")

    name_tags = browser.find_elements_by_xpath("//div[@class='td__nameWrapper']")
    dirty_name_tags = [x.text for x in name_tags]
    clean_names = []
    for dirty_tag in dirty_name_tags:
        split_string = dirty_tag.rsplit('(', 1)
        clean_names.append(split_string[0])
        # clean_names.append(dirty_tag)

    products = browser.find_elements_by_xpath("//tr[@class='tr__product']")
    list_of_specs = checkForEmpties(products)

    price_data = browser.find_elements_by_xpath("//td[@class='td__price']")

    names = [x.strip(' ') for x in clean_names]
    prices = [x.text for x in price_data]
    spec1 = [x[0] for x in list_of_specs]
    spec2 = [x[1] for x in list_of_specs]
    spec3 = [x[2] for x in list_of_specs]
    spec4 = [x[3] for x in list_of_specs]
    spec5 = [x[4] for x in list_of_specs]
    spec6 = [x[5] for x in list_of_specs]

    zipped_info = zip(names, spec1, spec2, spec3, spec4, spec5, spec6, prices)

    browser.close()

    return [list(x) for x in zipped_info]
    # return list_of_specs


def removeNewLines(scraped_list):
    output_list = []
    for item_spec in scraped_list:
        entry = []
        for element in item_spec:
            strippedEle = element.rstrip('\n')
            cleanedEle = strippedEle.split('\n')
            cleanStr = cleanedEle[-1]
            entry.append(cleanStr)
        output_list.append(entry)
    return output_list


def cleanDefault(stripped_list):
    return stripped_list


def cleanStorages(stripped_list):
    cleaned_list = []
    two_word_brands = ['Western Digital', 'Hyundai Technology', 'Silicon Power', 'Super Talent']
    for drive in stripped_list:
        if any(two_word_brand in drive[0] for two_word_brand in two_word_brands):
            name_split = drive[0].split(' ')
            brand = name_split[0] + " " + name_split[1]
            model = ""
            for remain in name_split[2:]:
                model += remain
        else:
            name_split = drive[0].split(' ', 1)
            brand = name_split[0]
            model = name_split[1]
        capacity = drive[1]
        price_per_gb = drive[2].lstrip('$')
        type = drive[3]
        cache = drive[4].rstrip(' MB')
        form_factor = drive[5]
        interface = drive[6]
        price_clean = drive[7].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append(
            [brand, model, capacity, price_per_gb, type, cache, form_factor, interface, price])
    return cleaned_list


def cleanCPUs(stripped_list):
    cleaned_list = []
    for cpu in stripped_list:
        name_split = cpu[0].split(' ', 1)
        brand = name_split[0]
        model = name_split[1]
        core_count = cpu[1]
        core_clock = cpu[2].rstrip(' GHz')
        boost_clock = cpu[3].rstrip(' GHz')
        tdp = cpu[4].rstrip(' W')
        integrated_graphics = cpu[5]
        smt = cpu[6]
        price_clean = cpu[7].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append(
            # [brand, model, size, width, height, ref_rate, res_rate, panel_type, asp_width, asp_height, price])
            [brand, model, core_count, core_clock, boost_clock, tdp, integrated_graphics, smt, price])
    return cleaned_list


def cleanMotherboards(stripped_list):
    cleaned_list = []
    for mb in stripped_list:
        name_split = mb[0].split(' ', 1)
        brand = name_split[0]
        model = name_split[1]
        socket = mb[1]
        form_factor = mb[2]
        mem_max = mb[3].rstrip(' GB')
        mem_slot = mb[4]
        color = mb[5]
        price_clean = mb[6].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append(
            # [brand, model, size, width, height, ref_rate, res_rate, panel_type, asp_width, asp_height, price])
            [brand, model, socket, form_factor, mem_max, mem_slot, color, price])
    return cleaned_list


def cleanPSUs(stripped_list):
    cleaned_list = []
    two_word_brands = ['Athena Power', 'be quiet!', 'Cooler Master', 'Fractal Design', 'FSP Group', 'In Win', 'Lian Li',
                       'Mars Gaming', 'Replace Power', 'Solid Gear', 'Super Flower']
    long_brand = 'PC Power & Cooling'

    for psu in stripped_list:
        if long_brand in psu[0]:
            name_split = psu[0].split(' ')
            brand = long_brand
            for remain in name_split[4:]:
                model += remain

        elif any(two_word_brand in psu[0] for two_word_brand in two_word_brands):
            name_split = psu[0].split(' ')
            brand = name_split[0] + " " + name_split[1]
            model = ""
            for remain in name_split[2:]:
                model += remain
        else:
            name_split = psu[0].split(' ', 1)
            brand = name_split[0]
            model = name_split[1]
        form_factor = psu[1]
        eff_rating = psu[2]
        wattage = psu[3].rstrip(' W')
        modular = psu[4]
        color = psu[5]
        price_clean = psu[6].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append(
            # [brand, model, size, width, height, ref_rate, res_rate, panel_type, asp_width, asp_height, price])
            [brand, model, form_factor, eff_rating, wattage, modular, color, price])
    return cleaned_list


def cleanRAMs(stripped_list):
    cleaned_list = []
    for ram in stripped_list:
        name_split = ram[0].split(' ', 1)
        if len(name_split) == 2:
            brand = name_split[0]
            model = name_split[1]
        else:
            brand = ram[0]
            model = "None"
        speed = ram[1]
        modules = ram[2]
        price_per_gb = ram[3].lstrip('$')
        color = ram[4]
        first_word_lat = ram[5].rstrip(' ns')
        cas_lat = ram[6]
        price_clean = ram[7].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append([brand, model, speed, modules, price_per_gb, color, first_word_lat, cas_lat, price])
    return cleaned_list


def cleanGPUs(stripped_list):
    cleaned_list = []
    for gpu in stripped_list:
        name_split = gpu[0].split(' ', 1)
        if len(name_split) == 2:
            brand = name_split[0]
            model = name_split[1]
        else:
            brand = gpu[0]
            model = "None"
        chipset = gpu[1]
        memory = gpu[2].rstrip(' GB')
        core_clock = gpu[3].rstrip(' MHz')
        boost_clock = gpu[4].rstrip(' MHz')
        color = gpu[5]
        length = gpu[6].rstrip(' mm')
        price_clean = gpu[7].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append(
            [brand, model, chipset, memory, core_clock, boost_clock, color, length, price])
    return cleaned_list


def cleanMonitors(stripped_list):
    cleaned_list = []
    two_word_brands = ['Cooler Master', 'Deco Gear', 'Fox Spirit', 'Titan Army', 'Wasabi Mango']
    for monitor in stripped_list:
        if any(two_word_brand in monitor[0] for two_word_brand in two_word_brands):
            name_split = monitor[0].split(' ')
            brand = name_split[0] + " " + name_split[1]
            model = ""
            for remain in name_split[2:]:
                model += remain
        else:
            name_split = monitor[0].split(' ', 1)
            brand = name_split[0]
            model = name_split[1]
        size = monitor[1].rstrip('"')
        resolution = monitor[2]
        # dim = monitor[2].split(' x ')
        # width = dim[0]
        # height = dim[1]
        ref_rate = monitor[3].rstrip(' Hz')
        res_rate = monitor[4].rstrip(' ms')
        panel_type = monitor[5]
        asp_ratio = monitor[6]
        # asp_split = monitor[6].split(':')
        # asp_width = asp_split[0]
        # asp_height = asp_split[1]
        price_clean = monitor[7].rstrip('Add')
        price = price_clean.lstrip('$')
        cleaned_list.append(
            # [brand, model, size, width, height, ref_rate, res_rate, panel_type, asp_width, asp_height, price])
            [brand, model, size, resolution, ref_rate, res_rate, panel_type, asp_ratio, price])
    return cleaned_list


def getAllPages(num_pages=2, category='monitors', base_url_pre='https://pcpartpicker.com/products/monitor/#',
                clean_function=cleanDefault, col_header=None):
    if col_header is None:
        col_header = monitor_col_header

    list_of_dfs = []

    for i in range(num_pages):
        url_iter = base_url_pre + "page=" + str(i + 1)
        original_list = get_browser_after_POST(base_url=url_iter)
        clean_list1 = removeNewLines(original_list)
        clean_list2 = clean_function(clean_list1)
        df = makeDf(clean_list2, col_header)
        list_of_dfs.append(df)

    df_aggregate = pd.concat(list_of_dfs, ignore_index=True)
    df_aggregate.to_csv('scraped/df_csvs/' + category + '.csv', index=False)
    return df_aggregate


def makeDf(cleaned_list, col_header):
    return pd.DataFrame(np.array(cleaned_list), columns=col_header)


def getSyncPage(base_url, num_pages, syncNum, syncType, col_header=monitor_col_header):
    list_of_dfs = []
    for i in range(num_pages):
        url_iter = base_url + '/#A=' + str(syncNum) + '&page=' + str(i + 1)
        original_list = get_browser_after_POST(url_iter)
        clean_list = removeNewLines(original_list)
        clean_list2 = cleanMonitors(clean_list)
        df = makeDf(clean_list2, col_header)
        list_of_dfs.append(df)
    df_aggregate = pd.concat(list_of_dfs, ignore_index=True)
    df_aggregate.to_csv('scraped/df_csvs/' + syncType + '.csv', index=False)
    return df_aggregate


def getCurved(base_url="https://pcpartpicker.com/products/monitor/", num_pages=3, col_header=monitor_col_header):
    list_of_dfs = []
    for i in range(num_pages):
        url_iter = base_url + '#C=1&page=' + str(i + 1)
        original_list = get_browser_after_POST(url_iter)
        clean_list = removeNewLines(original_list)
        clean_list2 = cleanMonitors(clean_list)
        df = makeDf(clean_list2, col_header)
        list_of_dfs.append(df)
    df_aggregate = pd.concat(list_of_dfs, ignore_index=True)
    df_aggregate.to_csv('scraped/df_csvs/curved.csv', index=False)
    return df_aggregate


def evaluateSync(a, b, c, d, e):
    if a == 1:
        return 'G sync'
    elif b == 1:
        return 'G sync Ultimate'
    elif c == 1:
        return 'Free Sync'
    elif d == 1:
        return 'Free Sync Premium'
    elif e == 1:
        return 'Free Sync Premium Pro'


def addSyncsToMonitors(csv_file_for_df):
    df = pd.read_csv(csv_file_for_df)
    df_g_sync = pd.read_csv("scraped/df_csvs/g_sync.csv")
    df_g_sync_ultimate = pd.read_csv("scraped/df_csvs/g_sync_ultimate.csv")
    df_free_sync = pd.read_csv("scraped/df_csvs/free_sync.csv")
    df_free_sync_premium = pd.read_csv("scraped/df_csvs/free_sync_premium.csv")
    df_free_sync_premium_pro = pd.read_csv("scraped/df_csvs/free_sync_premium_pro.csv")

    df = df.assign(gsync=df.model.isin(df_g_sync.model).astype(bool))
    df = df.assign(gsync_ultimate=df.model.isin(df_g_sync_ultimate.model).astype(bool))
    df = df.assign(free_sync=df.model.isin(df_free_sync.model).astype(bool))
    df = df.assign(free_sync_premium=df.model.isin(df_free_sync_premium.model).astype(bool))
    df = df.assign(free_sync_premium_pro=df.model.isin(df_free_sync_premium_pro.model).astype(bool))

    sync_list = [evaluateSync(a, b, c, d, e)
                 for a, b, c, d, e,
                 in zip(df['gsync'], df['gsync_ultimate'], df['free_sync'], df['free_sync_premium'],
                        df['free_sync_premium_pro'])]

    df['sync'] = sync_list
    df =df.drop(columns=['gsync', 'gsync_ultimate', 'free_sync', 'free_sync_premium', 'free_sync_premium_pro'])
    df.to_csv("cleaned/cleaned_monitors.csv", index=False)


def addCurvedAndCompatToMonitors(csv_file_for_df):
    df = pd.read_csv(csv_file_for_df)
    df_curved = pd.read_csv("scraped/df_csvs/curved.csv")
    df_g_sync_compat = pd.read_csv("scraped/df_csvs/g_sync_compat.csv")

    df = df.assign(curved=df.model.isin(df_curved.model).astype(bool))
    df = df.assign(g_sync_compat=df.model.isin(df_g_sync_compat.model).astype(bool))
    df.to_csv("cleaned/cleaned_monitors.csv", index=False)

