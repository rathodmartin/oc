<?xml version="1.0" encoding="UTF-8"?>
<!-- 
    Copyright (c) 2005, 2007 IBM Corporation and others.
    All rights reserved. This program and the accompanying materials
    are made available under the terms of the Eclipse Public License v1.0
    which accompanies this distribution, and is available at
    http://www.eclipse.org/legal/epl-v10.html
    Contributors:
    IBM Corporation - initial implementation
-->

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

	<xsl:template name="purposeSection">
		<xsl:param name="description"/>
		<xsl:variable name="purpose" select="$description/attribute[@name='purpose']"/>
		<xsl:if test="$purpose != ''">
			<div class="sectionHeading">
				<xsl:value-of select="$purposeText"/>
			</div>
			<div class="sectionContent">
				<table class="sectionTable" border="0" cellspacing="0" cellpadding="0">
					<tr valign="top">
						<td class="sectionTableSingleCell">
							<xsl:value-of disable-output-escaping="yes" select="$purpose"/>
						</td>
					</tr>
				</table>
			</div>
		</xsl:if>
	</xsl:template>

</xsl:stylesheet>
